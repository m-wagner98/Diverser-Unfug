puts "Knacke Passwort..."
p1 = "bewareoftheenigmagroupunderground"
p2 = "betterofftohacktherealownersboxes"
p3 = "wassaidbyadudepseudodpsychomarine"

characters = []

i = 0
p1.each_char do |ch|
    if (ch == p2[i]) || (ch == p3[i]) || (p2[i] == p3[i])
        characters.push(ch)
    end
    i = i+1
end
passwort = ""
characters.each do |c|
    passwort.concat(c)
end
puts "Passwort: #{passwort}"