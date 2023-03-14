M = {}


function Slice(tb, first, last, step) -- Slices of a Table.
    local sliced = {} 
    for i = first or 1, last or #tb, step or 1 do 
        sliced[#sliced+1] = tb[i]
    end
    return sliced
end
M.Slice = Slice

function M.Title(a) -- Titlecase
    a = tostring(a)
    return a:sub(1,1):upper()..a:sub(2)
end


function M.Clone(org) -- Duplicating Tables
    return {table.unpack(org)}
end

function M.Count(tbl, word) -- Word Count. -- DOESN'T WORK!
    local count = 0 
    local string = tbl
    for x in string:gmatch(word) do 
        count = count + 1  
    end
    return string, count
end

function M.Strip(String) 
    String = string.gsub(String, "%s+", "") 
    return String 
end

return M