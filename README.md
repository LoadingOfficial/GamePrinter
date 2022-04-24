# **GamePrinter**

**Simple python script _(by simple I mean over-engineered™)_ that sends game screenshots to the printer...**

_Windows only. (Sorry macOS and Linux users)

## FAQ
#### How?
The script checks for the latest screenshot in a specified folder and sends it to the printer.

#### Why?
~~Because it's fun.~~
Why not?

## Installation

0. Install [Python](https://python.org/)  on your system

1. Clone the repository.
    ```bash
    git clone <repo name>
    ```

2. Navigate into the directory
    ```bash
    cd "<repo name>-master"
    ```

3. Run the script
    ```bash
    python main.py
    ```

4. Edit the newly created `config.json` file with the path to your screenshots folder.
    Change any backslashes (`\`) to forward slashes (`/`) in the path.

    `config.json`
    ```json
    {
    "directory": "C:/path/to/screenshots/folder",
    "refresh_time": 5
    }
    ```
5. Run the script again.
    ```bash
    python main.py
    ```

6. *Enjoy!*

## To Do
- [ ] Add launch arguments support
- [ ] Make a config wizard to make it easier to setup
- [ ] Create a GUI
- [ ] Clean up the code
- [ ] Optimize the way I detect new files

## License
This project has the _I don't give a fuck what you do with the code as long as you credit me ^©^ ^patent^ ^pending^_ license.

> Feel free to screenshot!