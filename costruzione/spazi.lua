-- Inserisce un vero carattere "spazio" (largo zero) prima di ogni spazio tra parole:
-- l'aspetto della pagina non cambia, ma chi copia o estrae il testo vede le parole separate.
local GLYPH, GLUE, HLIST, VLIST, KERN, DISC = node.id("glyph"), node.id("glue"), node.id("hlist"), node.id("vlist"), node.id("kern"), node.id("disc")
local cache = {}
local function spacechar(f)
  if cache[f] == nil then
    local d = font.getfont(f)
    cache[f] = (d and d.characters and d.characters[32]) and true or false
  end
  return cache[f]
end
local function lastfont(n)
  local p = n.prev
  while p do
    if p.id == GLYPH then return p.font end
    if p.id == DISC or p.id == KERN then p = p.prev else return nil end
  end
end
local function nextisglyph(n)
  local q = n.next
  while q do
    if q.id == GLYPH or q.id == HLIST then return true end
    if q.id == KERN or q.id == DISC then q = q.next else return false end
  end
  return false
end
local function walk(head)
  local n = head
  while n do
    if n.id == HLIST then
      n.head = walk(n.head)
      local g = n.head
      while g do
        if g.id == GLUE and g.width > 0 and g.subtype ~= 8 and g.subtype ~= 9 then
          local f = lastfont(g)
          if f and spacechar(f) and nextisglyph(g) then
            local s = node.new(GLYPH); s.font = f; s.char = 32
            local w = font.getfont(f).characters[32].width or 0
            local k = node.new(KERN); k.kern = -w
            n.head = node.insert_before(n.head, g, s)
            n.head = node.insert_before(n.head, g, k)
          end
        end
        g = g.next
      end
    elseif n.id == VLIST then
      n.head = walk(n.head)
    end
    n = n.next
  end
  return head
end
luatexbase.add_to_callback("pre_shipout_filter", function(box) box.head = walk(box.head); return true end, "spazi veri")
