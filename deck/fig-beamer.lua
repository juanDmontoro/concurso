-- fig-beamer.lua — anchos de figura propios de la salida beamer.
--
-- Los decks fuente fijan el ancho de cada figura pensando en RevealJS
-- (1920 px). Alguna figura muy apaisada queda pequeña en el frame beamer
-- (16:9, texto a 8pt) con ese mismo porcentaje. Aquí se sobrescribe el
-- ancho solo en beamer, por nombre de archivo (sin extensión), sin tocar
-- los decks fuente (solo lectura).

if not FORMAT:match("beamer") then
  return {}
end

local ANCHOS = {
  fig_metodologia = "100%",  -- Parte 2, «Metodología docente: secuencia de aprendizaje» (900×185, 64% en reveal)
}

function Image(img)
  local nombre = img.src:match("([^/]+)%.%w+$")
  local ancho = nombre and ANCHOS[nombre]
  if ancho then
    img.attributes.width = ancho
    return img
  end
end
