10.132.16.2
E:\temp

xcopy \\10.132.16.2\e$\temp\Test.bat D:\Temp /f /j /v /y /z

xcopy \\10.9.5.81\f$\text.* D:\Temp /f /j /v /y /z


xcopy \\10.9.5.81\c$\Planview\MidTier\Logs\pvtrace.2017-05-03.* D:\Temp /f /j /v /y /z


/f = This option will display the full path and file name of both the source and destination files being copied.

/i = Use the /i option to force xcopy to assume that destination is a directory. If you don't use this option, and you're copying from source that is a directory or group of files and copying to destination that doesn't exist, the xcopy command will prompt you enter whether destination is a file or directory.

/j = This option copies files without buffering, a feature useful for very big files. This xcopy command option was first available in Windows 7.

/l = Use this option to show a list of the files and folders to copied... but no copying is actually done. The /l option is useful if you're building a complicated xcopy command with several options and you'd like to see how it would function hypothetically.

/u = This option will only copy files in source that are already in destination.

/v = This option verifies each file as it's written, based on its size, to make sure they're identical. Verification was built in to the xcopy command beginning in Windows XP, so this option does nothing in later versions of Windows and is only included for compatibility with older MS-DOS files.

/y = Use this option to stop the xcopy command from prompting you about overwriting files from source that already exist in destination.

/z = This option allows the xcopy command to safely stop copying files when a network connection is lost and then resume copying from where it left off once the connection is reestablished. This option also shows the percentage copied for each file during the copy process.
