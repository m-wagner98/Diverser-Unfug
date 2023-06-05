write "keep screen awake script is running..."
$myshell = New-Object -com "Wscript.Shell"
while (1) {$myshell.sendkeys("{F15}"); sleep 30}