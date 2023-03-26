# Passwordsy
A program that can generate a secure password of up to 100 characters (with uppercase and lowercase letters, digits, and/or punctuation), and check for vulnerabilities (prevalence, length, complexity, repetitiveness) in a given password.

Blog: https://icethedev2.github.io/

## Coming soon...
<a data-flickr-embed="true" href="https://www.flickr.com/photos/197764307@N08/52722054145/in/dateposted-public/" title="23"><img src="https://live.staticflickr.com/65535/52722054145_71f6e09590_c.jpg" width="800" height="269" alt="23"></a>
- New password generation modes, including diceware
- Hiding passwords


## Getting started
To use Passwordsy, you must get the program itself on your machine. To do this, you have 3 choices: clone it through Git, open it with GitHub desktop, or download it as a ZIP. The following tutorial describes installing Passwordsy by cloning the repository with Git.

### Prerequisites
You will need to install Python (from the Microsoft Store, for example) and GitHub Desktop to run this program.

- Git from git-scm.com.
- Python from python.org (make sure to tick 'Add python to PATH').
- The following modules: PIL, Clipboard, Pynput. Install them through the following commands in the Git Bash terminal:

python -m pip install pillow

python -m pip install clipboard

python -m pip install pynput

### Installation
- Find the absolute path to Python on your machine (it could be C:\Users\Cristi\AppData\Local\Programs\Python\Python311 on Windows, for example).
- Open Git Bash.
- Use cd (change directory) to move to the location you want the repository to be cloned in. For example, if you want the repository to be cloned in the ‘passwordsy’ folder on Desktop, type ‘cd Desktop/passwordsy/‘ in the - terminal.
- Once you are in the desired folder, type ‘git clone https://github.com/IceTheDev2/Passwordsy.git’.
- Type ‘cd Passwordsy/code’ to the navigate to the file containing main.py.
- Type ‘python main.py’ to run the program.


## Usage
You can use this program to generate a random secure string of 4 to 100 uppercase and lowercase letters, numbers and/or punctuation marks.
![alt_text](https://github.com/IceTheDev2/Passwordsy/blob/main/code/screenshots/1.PNG)
![alt_text](https://github.com/IceTheDev2/Passwordsy/blob/main/code/screenshots/2.PNG)
![alt_text](https://github.com/IceTheDev2/Passwordsy/blob/main/code/screenshots/3.PNG)


You can also use it to discover weaknesses of a password, such as prevalence, length, simplicity, repeating characters.
![alt_text](https://github.com/IceTheDev2/Passwordsy/blob/main/code/screenshots/4.PNG)
![alt_text](https://github.com/IceTheDev2/Passwordsy/blob/main/code/screenshots/5.PNG)
![alt_text](https://github.com/IceTheDev2/Passwordsy/blob/main/code/screenshots/6.PNG)


## Contributing
I'd love to hear your suggestions on how I can improve my first project!  
You can fork the project to play around with it and create a pull request to submit your suggestions. You can also open an issue to tell me about any problems my code might have.

## License
This project is licensed under the MIT License. Read LICENSE.txt for more information.

## Contact
Project Link: https://github.com/IceTheDev2/Passwordsy/  

Reddit: https://www.reddit.com/user/AnEntirePeach

Youtube: https://www.youtube.com/channel/UCBqVJU4gjeik1RavAsVR6Pg

E-mail: icethedev2@gmail.com

## Acknowledgements
* The [r/Python](https://www.reddit.com/r/Python/), [r/learnprogramming](https://www.reddit.com/r/learnprogramming/) and [r/learnpython](https://www.reddit.com/r/learnpython/) communities on Reddit for providing me with great tips and suggestions
* The GitHub contributors to this project, [dwaffle](https://github.com/dwaffle), [christopher-chandler](https://trello.com/c/f72vJsYk/50-https-githubcom-christopher-chandler), and [MartinMerkli](https://github.com/MartinMerkli)
* [u/creedxender](https://www.reddit.com/user/creedxender/) for suggesting a 'Secret string of letters, numbers, and/or symbols'.
* [u/infra_d3ad](https://www.reddit.com/user/infra_d3ad/) for suggesting using diceware.
* [u/modernknight87](https://www.reddit.com/user/modernknight87/) for suggesting 'The user input a sentence of their own choosing, takes the first letter of every word, and any numbers or symbols, and combines those as the produced password'.
* The [codemy.com Youtube channel](https://www.youtube.com/@Codemycom) for their great Tkinter tutorials, such as: [this one on keyboard event binding](https://youtu.be/GLnNPjL1U2g), [this one on cursor positions](https://youtu.be/Z4zePg2M5H8), [this one on Tkinter menus](https://youtu.be/KRuUtNxOb_k), [this one on message boxes](https://youtu.be/S3AaSwpb5GE).
* The [SecLists repository](https://github.com/danielmiessler/SecLists) of danielmiessler, used here for the 100,000 most common passwords.
* The [diceware repository](https://github.com/ulif/diceware) of ulif, used here to generate for a unique password-generation mode.
* The [CustomTkinter repository](https://github.com/TomSchimansky/CustomTkinter) of Tom Schimansky, used here for the UI overhaul.
* [Exercism](https://exercism.org/) for its large array of exercises
* [ChatGPT](https://chat.openai.com/chat) for helping me solve the most obscure of errors and bugs.
* These Stack Overflow questions for clarifying certain errors and concepts: https://stackoverflow.com/questions/61139160/tkinter-error-tkinter-tclerror-invalid-command-name-frame-entry-python, https://stackoverflow.com/questions/45847313/what-does-weight-do-in-tkinter, as well as a ton others scattered around the code.
* [This tutorialspoint.com page](https://www.tutorialspoint.com/how-to-delete-tkinter-widgets-from-a-window#:~:text=We%20can%20delete%20widgets%20from,defining%20a%20function%20for%20it.), [this one](https://www.tutorialspoint.com/how-can-i-identify-when-a-button-is-released-in-tkinter), as well as others.
* Paul Miskew for his [PYTHON 3 TKINTER - GUI ENTRY BIND KEY](https://youtu.be/JThKYGapGzU) video
* [This simplilearn.com page](https://www.simplilearn.com/tutorials/python-tutorial/python-typeof-function)
* [This realpython.com page](https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings)
* [This flexiple.com page](https://flexiple.com/python/python-list-contains/)
* [This Runestone Academy page](https://runestone.academy/ns/books/published/fopp/SimplePythonData/UpdatingVariables.html#:~:text=In%20Python%20%2B%3D%20is%20used,or%20x%20%3D%20x%20%2B%201%20.)
* [This geeksforgeeks.org page](https://www.geeksforgeeks.org/append-extend-python/#:~:text=What%20is%20Append%20in%20Python,the%20end%20of%20a%20list.)
* [This digitalocean.com page](https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3)
* [This edureka.co page](https://www.edureka.co/community/33869/how-to-use-not-equal-operator-in-python#:~:text=You%20can%20use%20%22!%3D,are%20not%20equal%2C%20otherwise%20false%20.)
* [This GitHub Docs page](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/approving-a-pull-request-with-required-reviews)
* [This video by plus 2 net](https://youtu.be/mSpLnnXeiIc)
* [This video from PyTutorials](https://youtu.be/DTnz8wA6wpw)
* [This video from Appficial](https://youtu.be/eszrY7w83q8) for clarifying f-strings for me.
* [This W3Schools page](https://www.w3schools.com/python/python_dictionaries.asp)
