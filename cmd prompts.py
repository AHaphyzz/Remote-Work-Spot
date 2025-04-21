import pandas as pd

# Define the data
data = [
    # File & Directory Management
    ["File & Directory Management", "List files in directory", "dir", "Get-ChildItem or ls", "ls"],
    ["File & Directory Management", "List all (including hidden)", "dir /a", "Get-ChildItem -Force", "ls -a"],
    ["File & Directory Management", "Change directory", "cd <path>", "Set-Location <path>", "cd <path>"],
    ["File & Directory Management", "Go up one directory", "cd ..", "cd ..", "cd .."],
    ["File & Directory Management", "Create a directory", "mkdir <dir_name>", "New-Item -ItemType Directory <dir_name>", "mkdir <dir_name>"],
    ["File & Directory Management", "Remove a directory", "rmdir <dir_name>", "Remove-Item <dir_name> -Recurse", "rm -r <dir_name>"],
    ["File & Directory Management", "Delete a file", "del <file>", "Remove-Item <file>", "rm <file>"],
    ["File & Directory Management", "Copy a file", "copy <source> <dest>", "Copy-Item <source> <dest>", "cp <source> <dest>"],
    ["File & Directory Management", "Move/Rename a file", "move <source> <dest>", "Move-Item <source> <dest>", "mv <source> <dest>"],

    # System Information & Process Management
    ["System Information & Process Management", "Show current directory", "cd", "Get-Location", "pwd"],
    ["System Information & Process Management", "Show running processes", "tasklist", "Get-Process", "ps aux"],
    ["System Information & Process Management", "Kill a process", "taskkill /F /PID <id>", "Stop-Process -Id <id>", "kill <id> or pkill <name>"],
    ["System Information & Process Management", "Show system information", "systeminfo", "Get-ComputerInfo", "uname -a or hostnamectl"],
    ["System Information & Process Management", "Show disk usage", "dir", "Get-PSDrive", "df -h"],

    # Networking Commands
    ["Networking Commands", "Check network status", "ipconfig", "Get-NetIPAddress", "ifconfig or ip a"],
    ["Networking Commands", "Test network connection", "ping <website>", "Test-Connection <website>", "ping <website>"],
    ["Networking Commands", "Show active connections", "netstat -an", "Get-NetTCPConnection", "netstat -an"],
    ["Networking Commands", "Get DNS info", "nslookup <website>", "Resolve-DnsName <website>", "dig <website> or nslookup"],

    # File Viewing & Editing
    ["File Viewing & Editing", "View text file contents", "type <file>", "Get-Content <file>", "cat <file>"],
    ["File Viewing & Editing", "Edit a file (basic editor)", "notepad <file>", "notepad <file>", "nano <file> or vim <file>"],
    ["File Viewing & Editing", "Search inside files", 'find "text" <file>', 'Select-String "text" <file>', 'grep "text" <file>'],

    # User & Permissions
    ["User & Permissions", "Show current user", "whoami", "$env:UserName", "whoami"],
    ["User & Permissions", "List users", "net user", "Get-LocalUser", "cat /etc/passwd"],
    ["User & Permissions", "Change file permissions", "icacls <file> /grant", "Set-Acl", "chmod 755 <file>"],

    # Miscellaneous
    ["Miscellaneous", "Clear screen", "cls", "Clear-Host", "clear"],
    ["Miscellaneous", "Exit command line", "exit", "exit", "exit"],
    ["Miscellaneous", "Run as administrator", "runas /user:admin", "Start-Process PowerShell -Verb RunAs", "sudo <command>"]
]

# Define the CSV file name
csv_file = "command_line_commands.csv"

df = pd.DataFrame(data, columns=["Categories", "Action", "Windows (CMD)", "PowerShell", "Linux/Mac OS"])
df.to_csv(csv_file, index=False)
