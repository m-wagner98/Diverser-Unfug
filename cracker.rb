require_relative "crypter_scrypt"

hash = ARGV[0]
wortlisteDatei = ARGV[1]
transformationDateiString = ARGV[2]

#Probiere alle Wörter in wortliste
puts "Teste gegen Wortliste #{wortlisteDatei}"
wortlisteString = IO.read(wortlisteDatei)
wortliste = wortlisteString.split(' ')
a = Time.now
wortliste.each do |wort|
    if ARGV[3]
        puts wort
    end
    if test_password(wort, hash)
        puts "Gefunden: #{wort}"
        exit 0
    end
end
b = Time.now
puts "Laufzeit: #{b-a}s"
puts
puts

#Probiere die Worte mit Modifikationen
puts "Teste gegen modifizierte Wortliste"

transformationDatei = IO.read("#{transformationDateiString}")
transDateiArray = transformationDatei.split("\n")
a = Time.now
wortliste.each do |wort|
    transDateiArray.each do |line|
        lineArray = line.split(' ')
        regexp = Regexp.new(eval(lineArray[0]))
        char = lineArray[1].to_s
        wortMod = wort.gsub(regexp, char)
        if ARGV[3] === "-v"
            puts wortMod
        end
        if test_password(wortMod, hash)
            puts "Gefunden: #{wortMod}"
            exit 0
        end
    end
end
b = Time.now
puts "Laufzeit: #{b-a}s"
puts
puts

#Starte BruteForce Angriff
#Erzeuge Array mit zu probierenden Zeichen
zeichen = ('A'..'Z').to_a
('a'..'z').each do |char|
    zeichen << char
end
(0..9).each do |ziffer|
    zeichen << ziffer
end
zeichen << "!" << "" << "§" << "%" << "$" << "/" << "{" << "(" << "[" << ")" << "]" << "=" << "}" << "?" << "\\" << "`" << "´"
zeichen << "*" << "+" << "~" << "'" << "#" << "-" << "_" << ">" << "<" << "|" << "°" << ";" << "," << "." << ":"
#
maxPasswortLänge = 10 #maximale Länge des Bruteforce Angriffs festlegen
1.upto(maxPasswortLänge) do |i|
    puts "Brute Force Angriff Länge #{i}"
    a = Time.now
    permutation = zeichen.repeated_permutation(i).to_a
    permutation.each do |p|
    pw = p.reduce("") {|string, g| string + g.to_s}
    if ARGV[3] === "-v"
        puts pw
    end
    if test_password(pw, hash)
        puts "Gefunden: #{pw}"
        b = Time.now
        puts "Laufzeit: #{b-a}s"
        exit 0
    end    
    end
    b = Time.now
    puts "Laufzeit: #{b-a}s"
    puts
end

#GU9hnu6zy1epLKlatP95eg==|MWU3ZjJjMmY4NTI5MDA5YmQ2Y2M0OTYyN2Y2ZmI5ODU= #Schmetterling
#Qfgf3j0NmFfs3i9pviMqqA==|NGY5NmVhNGE2YTM2NDFhNDgyNTE1ODVhNTkyZjk3ZGI= #V3rsich3rungsb3trug
#tvzL+q2OH9/nRx28hsIamA==|NGVhZTk3ZGI2M2QyY2RmNGVmNDEzZmNjMDE3NGIxMTY= #a%bc

#O8Od9OJpwEDi1fxhAEkuWQ==|rWCtY7zidb91yiQyHh4duQSb8NL21hF9SZpAf8VDEDc= #(scrypt)
#Dauert ewig, geht net