-- row-rules.lua — filetes finos entre filas del cuerpo de las tablas,
-- solo en la salida beamer (el HTML ya dibuja las filas vía CSS).
-- Requiere \lightrowrule definido en include-in-header del qmd.

if FORMAT ~= "beamer" then
  return {}
end

function Table(el)
  local tex = pandoc.write(pandoc.Pandoc({ el }), "latex")
  local _, head_end = tex:find("\\endhead\n", 1, true)
  if not head_end then
    return nil
  end
  local head = tex:sub(1, head_end)
  local body = tex:sub(head_end + 1)
  -- Cada fila del cuerpo termina en "\\" + salto de línea.
  body = body:gsub("\\\\\n", "\\\\ \\lightrowrule\n")
  -- Sin filete extra pegado al \bottomrule de cierre.
  body = body:gsub("\\lightrowrule\n\\bottomrule", "\\bottomrule")
  return pandoc.RawBlock("latex", head .. body)
end
