function City_country(tbl)
    --[[ A City Inside a Country ]]--
    setmetatable(tbl, {__index={population=""}})
    local city, country, population = 
    tbl[1] or tbl.city, 
    tbl[2] or tbl.country, 
    tbl[3] or tbl.population
    Places = {}
    if population then
        Places[city] = country
        Places['population'] = population
        for cities, countries in pairs(Places) do
            Place = (cities..", "..countries.." - ".."population "..
            tostring(Places['population'])) 
            print(Place)
            return Place
        end
    else
        Places[city] = country 
        for cities, countries in pairs(Places) do
            Place = cities..", "..countries
            print(Place)
            return Place
        end
    end
end
