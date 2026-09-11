-- roadmap.lua — mapa de progreso jerárquico (partes › secciones › subsecciones)
-- en los divisores de parte y en las diapositivas de sección del deck unificado.
--
-- Estructura que lee del documento fusionado (tras el filtro `quarto`):
--   * Divisor de parte: cabecera de nivel 1 con clase `part-divider`
--     (`# Currículum {.part-divider}` en el maestro). El filtro añade el
--     eyebrow «Parte N de M» y la línea de partes; en beamer lo sustituye
--     por \partdividercontent{eyebrow}{título}{línea de partes}.
--   * Sección: cualquier otra cabecera de nivel 1 dentro de una parte. Si en
--     una parte alguna cabecera lleva la clase `roadmap-slide` (Parte 3),
--     solo participan las que la llevan (excluye el título de la propuesta).
--   * Subsección: un título «Grupo · Detalle» se agrupa con sus vecinos del
--     mismo grupo («Resultados · Predicción» → sección «Resultados», sub
--     «Predicción»), replicando el mapa de dos niveles del deck fuente.
--   * Los divs `.roadmap` que traen los decks fuente se eliminan: el mapa se
--     regenera aquí con la jerarquía completa (y en beamer evitaban un frame
--     espurio tras cada página de sección).
--
-- Salida revealjs: divs `.roadmap.parts`, `.roadmap` y `.roadmap.sub` con
-- spans `.step`/`.step.active` (CSS en el include-in-header del maestro).
-- Salida beamer: \gdef\roadmapcontent{...} antes de cada \section, que la
-- plantilla «section page» del maestro imprime bajo la barra de progreso.

local SEP = " · "

local function is_header(b, level)
  return b.t == "Header" and b.level == level
end

local function split_group(title)
  local g, s = title:match("^(.-)%s+·%s+(.+)$")
  if g then return g, s end
  return title, nil
end

-- ---------------------------------------------------------------- estructura

local function leer_estructura(blocks)
  local parts = {}
  local current = nil
  for i, b in ipairs(blocks) do
    if is_header(b, 1) and b.classes:includes("part-divider") then
      current = { idx = i, title = pandoc.utils.stringify(b), inlines = b.content,
                  sections = {} }
      table.insert(parts, current)
    elseif is_header(b, 1) and current then
      table.insert(current.sections, {
        idx = i, title = pandoc.utils.stringify(b),
        marked = b.classes:includes("roadmap-slide"),
      })
    end
  end
  for _, p in ipairs(parts) do
    local marked = {}
    for _, s in ipairs(p.sections) do
      if s.marked then table.insert(marked, s) end
    end
    if #marked > 0 then p.sections = marked end
    -- Agrupación «Grupo · Detalle» en entradas de primer nivel con subpasos.
    p.entries = {}
    for _, s in ipairs(p.sections) do
      local g, sub = split_group(s.title)
      s.group, s.sub = g, sub
      local last = p.entries[#p.entries]
      if sub and last and last.label == g then
        table.insert(last.subs, s)
      else
        local e = { label = g, subs = {} }
        if sub then table.insert(e.subs, s) end
        table.insert(p.entries, e)
      end
      s.entry = p.entries[#p.entries]
    end
  end
  return parts
end

-- ------------------------------------------------------------------ revealjs

local function step(text, active)
  local classes = { "step" }
  if active then table.insert(classes, "active") end
  return pandoc.Span(pandoc.Inlines(text), pandoc.Attr("", classes))
end

local function linea(items, classes)
  local inl = pandoc.Inlines({})
  for k, it in ipairs(items) do
    if k > 1 then inl:extend(pandoc.Inlines(SEP)) end
    inl:insert(step(it.text, it.active))
  end
  return pandoc.Div({ pandoc.Plain(inl) }, pandoc.Attr("", classes))
end

local function linea_partes_html(parts, n)
  local items = {}
  for k, p in ipairs(parts) do
    items[k] = { text = "Parte " .. k .. SEP .. p.title, active = (k == n) }
  end
  return linea(items, { "roadmap", "parts" })
end

local function mapa_seccion_html(parts, n, s)
  local p = parts[n]
  local out = { linea_partes_html(parts, n) }
  local items = {}
  for k, e in ipairs(p.entries) do
    items[k] = { text = e.label, active = (e == s.entry) }
  end
  table.insert(out, linea(items, { "roadmap" }))
  if #s.entry.subs > 0 then
    local subs = {}
    for k, ss in ipairs(s.entry.subs) do
      subs[k] = { text = ss.sub, active = (ss == s) }
    end
    table.insert(out, linea(subs, { "roadmap", "sub" }))
  end
  return out
end

-- -------------------------------------------------------------------- beamer

local function tex(inlines_or_text)
  local inl = type(inlines_or_text) == "string"
    and pandoc.Inlines(inlines_or_text) or inlines_or_text
  local s = pandoc.write(pandoc.Pandoc({ pandoc.Plain(inl) }), "latex")
  return (s:gsub("%s+$", ""))
end

-- \mbox: cada paso es indivisible; la línea solo se parte entre pasos.
local function step_tex(text, active)
  if active then
    return "\\mbox{\\color{mDarkTeal}\\bfseries " .. tex(text) .. "}"
  end
  return "\\mbox{\\color{black!40}" .. tex(text) .. "}"
end

local function linea_tex(items, size, sep)
  local t = {}
  for k, it in ipairs(items) do t[k] = step_tex(it.text, it.active) end
  return "{" .. size .. " " .. table.concat(t, sep) .. "\\par}"
end

local function linea_partes_tex(parts, n)
  local items = {}
  for k, p in ipairs(parts) do
    items[k] = { text = "Parte " .. k .. SEP .. p.title, active = (k == n) }
  end
  return linea_tex(items, "\\scriptsize", "\\quad ")
end

local function mapa_seccion_tex(parts, n, s)
  local p = parts[n]
  local out = { linea_partes_tex(parts, n), "\\vspace{0.8em}" }
  local items = {}
  for k, e in ipairs(p.entries) do
    items[k] = { text = e.label, active = (e == s.entry) }
  end
  table.insert(out, linea_tex(items, "\\large", "~· "))
  if #s.entry.subs > 0 then
    local subs = {}
    for k, ss in ipairs(s.entry.subs) do
      subs[k] = { text = ss.sub, active = (ss == s) }
    end
    table.insert(out, "\\vspace{0.2em}")
    table.insert(out, "\\hspace{1.5em}" .. linea_tex(subs, "\\normalsize", "~· "))
  end
  return table.concat(out, "\n")
end

-- ------------------------------------------------------------------- filtro

function Pandoc(doc)
  local parts = leer_estructura(doc.blocks)
  if #parts == 0 then return nil end
  local beamer = FORMAT:match("beamer") ~= nil

  -- Índices: bloque → (parte, sección)
  local divider_at, section_at = {}, {}
  for n, p in ipairs(parts) do
    divider_at[p.idx] = n
    for _, s in ipairs(p.sections) do section_at[s.idx] = { n = n, s = s } end
  end

  local out = pandoc.List()
  for i, b in ipairs(doc.blocks) do
    if b.t == "Div" and b.classes:includes("roadmap") then
      -- descartado: se regenera abajo
    elseif divider_at[i] then
      local n = divider_at[i]
      local eyebrow = "Parte " .. n .. " de " .. #parts
      if beamer then
        out:insert(pandoc.HorizontalRule())
        out:insert(pandoc.RawBlock("latex",
          "\\partdividercontent{" .. eyebrow .. "}{" .. tex(b.content) .. "}{"
          .. linea_partes_tex(parts, n) .. "}"))
      else
        local inl = pandoc.Inlines({
          pandoc.Span(pandoc.Inlines(eyebrow), pandoc.Attr("", { "part-eyebrow" })),
          pandoc.Space() })
        inl:extend(b.content)
        b.content = inl
        if not b.classes:includes("center") then b.classes:insert("center") end
        out:insert(b)
        out:insert(linea_partes_html(parts, n))
      end
    elseif is_header(b, 1) and beamer then
      local hit = section_at[i]
      local body = hit and mapa_seccion_tex(parts, hit.n, hit.s) or ""
      -- \gdef sobrevive al grupo del frame anterior en el que Pandoc lo inserta.
      out:insert(pandoc.RawBlock("latex", "\\gdef\\roadmapcontent{" .. body .. "}"))
      out:insert(b)
    elseif section_at[i] then
      local hit = section_at[i]
      if not b.classes:includes("roadmap-slide") then b.classes:insert("roadmap-slide") end
      out:insert(b)
      for _, d in ipairs(mapa_seccion_html(parts, hit.n, hit.s)) do out:insert(d) end
    else
      out:insert(b)
    end
  end
  doc.blocks = out
  return doc
end
