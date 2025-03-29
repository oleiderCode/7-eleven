[Setup]
AppName=Tickets_gio
AppVersion=1.0
DefaultDirName={pf}\Tickets_gio
DefaultGroupName=Tickets_gio
UninstallDisplayIcon={app}\Tickets_gio.exe
Compression=lzma
SolidCompression=yes
OutputDir=.
OutputBaseFilename=Tickets_gio_Instalador

[Files]
Source: "dist\Tickets_gio.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "hand.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Tickets_gio"; Filename: "{app}\Tickets_gio.exe"; IconFilename: "{app}\hand.ico"
Name: "{commondesktop}\Tickets_gio"; Filename: "{app}\Tickets_gio.exe"; IconFilename: "{app}\hand.ico"

[Run]
Filename: "{app}\Tickets_gio.exe"; Description: "Ejecutar Tickets_gio"; Flags: nowait postinstall skipifsilent
