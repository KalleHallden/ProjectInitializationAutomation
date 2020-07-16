## Pre-setup:

### Create user variables

#### Manually
```
Go to 
> environment vairables
> Click "New" in User variables (the top one)
> Set name as "PWFA-Path"
> Set value as your workspace path
> Get a token here: https://github.com/settings/tokens/new
  > Must have repo, user, and delete_repo permissions
> Set "PWFA-Token" to the given token.
```
#### Through CMD
```
> setx [user variable name] "[user variable token]

For example:
> setx PWFA-Path "ThisIsMyTokenInQuotes"
```
Either way, you'll have to reset your pc before using them.
## Setup: 
```bash
git clone "https://github.com/Red-CS/ProjectInitializationAutomation.git"
cd projectInitializerAutomation
pip install -r requirements.txt

If you are on Windows, which you probably are, be sure to add the "projectInitializerAutomation\windows_OS" 
folder directory to path, instead you will use the files meant for Mac
```

## Usage:
#### General Use

Basically, the core of the command is this:
```
create <repository name> [options]
```
The repository name can now have spaces! Just be sure to put them in quotes:
```
create "Subscribe to Kalle Halden"
```
#### Descriptions
Additonally, it's nice to give you're repository a description, yeah? You can type:
```
create "Subscribe to Kalle Halden" -d "Remember to like and comment"
OR
create "Subscribe to Kalle Halden" --description "Share with your friends!"
```
#### Private Repositories
Want to set your repo to private? Just add -p or --private
```
create "Subscribe to Kalle Halden" -d "Like the video" -p.
> Initializes a Github repository set to private.
```
Don't include this tag for public repos, those are the default.
#### Local Repositories
Creating a local repository is as simple as typing:
```
create "My Local Repository" -l
OR
create "My Local Repository" --local
```
Note that it follows that strict syntax (create [repo name] -l/--local)

## Example
Say I wanted to build a remote repository named "Subscribe to Kalle Halden" with a description of "Leave a like and comment!" We'll set as public, too. Just type:
```
create "Subscribe to Kalle Halden" -d "Leave a like and comment!"
```
You'll see a message on Command prompt that looks like this:
```
The following arguments will be passed:
  Name:                 Subscribe to Kalle Halden
  Description:          Leave a like and comment!
  Publicity:            Public

Is this information correct (y/n)? 
```
Simply type "y" or "Y" and your remote Repository will be instantiated.

If you want to skip that auto confirmation, just add one of the following to the end of the command:
```
-y     --yes     --auto-confirm
```
I recommend doing this for longer repository names and descriptions.

## Troubleshooting and Help
If you ever need more info on a tag, type either:
```
-h     --help     help()
```
after a tag. For example:
```
create -d -h
> Outputs description tag usage
```
Additionally, just typing
```
create
OR
create -h / --help / help()
```
will bring up general usage for all tags and commands.

