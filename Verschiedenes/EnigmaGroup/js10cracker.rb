def checkPass (password)
    count1 = 3; count2 = 5
    sumof1 = 0; sumof2 = 0

    charlist = "BHFE8"

    password.each_char do |c|
        sumof1 = sumof1 + (c.ord * count1)
        count1 = count1 + 1
    end

    charlist.each_char do |c|
        sumof2 = sumof2 + (c.ord * count2)
        count2 = count2 + 1
    end

    if sumof1 == sumof2 then
        true
    end
    nil
end
############################crack password with bruteforce######################################
#create base
base = ('A'..'Z').to_a
('a'..'z').each do |x|
    base << x
end
(0..9).each do |d|
    base << d
end
#crack
maximumPasswordLength = 10
1.upto(maximumPasswordLength) do |i|
    puts "Angriff Länge #{i}"
    permutation = base.repeated_permutation(i).to_a
    permutation.each do |p|
        pw = p.reduce("") {|string, g| string + g.to_s} #convert permutation values to string
        if checkPass(pw) then
            puts "Passwort: #{pw}"
            exit 0
        end
    end
end