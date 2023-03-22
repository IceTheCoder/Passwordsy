# Passwordsy
A program that can generate a secure password of up to 100 characters (with uppercase and lowercase letters, digits, and/or punctuation), and check for vulnerabilities (prevalence, length, complexity, repetitiveness) in a given password.

Blog: https://icethedev2.github.io/

## Getting started
To use Passwordsy, you must get the program itself on your machine. To do this, you have 3 choices: clone it through Git, open it with GitHub desktop, or download it as a ZIP. The following tutorial describes installing Passwordsy by cloning the repository with Git.

### Prerequisites
- Git from git-scm.ro
- Python from python.org (make sure to tick 'Add Python to PATH')
- The following modules: PIL, Clipboard, Pynput.

Install them through the following commands in the Git Bash terminal:

python -m pip install pillow

python -m pip install clipboard

python -m pip install pynput


### Installation
- Open Git Bash
- Use cd (change directory) to move to the location you want the repository to be cloned in. For example, if you want the repository to be cloned in the ‘passwordsy’ folder on Desktop, type ‘cd Desktop/passwordsy/‘ in the terminal.
- Once you are in the desired folder, type ‘git clone https://github.com/IceTheDev2/Passwordsy.git’.
- Type ‘cd Passwordsy/code’ to the navigate to the file containing main.py.
- Type ‘python main.py’ to run the program


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
* The [codemy.com Youtube channel](https://www.youtube.com/@Codemycom) for their great Tkinter tutorials, such as [this one on keyboard event binding](https://youtu.be/GLnNPjL1U2g), [this one on cursor positions](https://youtu.be/Z4zePg2M5H8), and [this one on Tkinter menus](https://youtu.be/KRuUtNxOb_k)
* The GitHub contributors to this project, [dwaffle](https://github.com/dwaffle), [christopher-chandler](https://trello.com/c/f72vJsYk/50-https-githubcom-christopher-chandler), and [MartinMerkli](https://github.com/MartinMerkli)
* The [SecLists repository](https://github.com/danielmiessler/SecLists) of danielmiessler, used here for the 100,000 most common passwords
* [Exercism](https://exercism.org/) for its large array of exercises
* [ChatGPT](https://chat.openai.com/chat) for helping me solve the most obscure of errors and bugs.
* These Stack Overflow questions: https://stackoverflow.com/questions/2260235/how-to-clear-the-entry-widget-after-a-button-is-pressed-in-tkinter, https://stackoverflow.com/questions/68327/change-command-method-for-tkinter-button-in-python, https://stackoverflow.com/questions/61139160/tkinter-error-tkinter-tclerror-invalid-command-name-frame-entry-python, https://stackoverflow.com/questions/45847313/what-does-weight-do-in-tkinter, https://stackoverflow.com/questions/66035176/entry-widget-in-tkinter-with-key-bind, https://stackoverflow.com/questions/66035176/entry-widget-in-tkinter-with-key-bind, https://stackoverflow.com/questions/69425865/tkinter-event-x-y-mouse-position-wrong-value-only-when-mouse-movement-up, https://stackoverflow.com/questions/68615095/how-do-i-find-the-position-of-a-widget-relative-to-the-window-in-tkinter, https://stackoverflow.com/questions/45393923/python-tkinter-key-binding-to-all-subsequent-widgets, https://stackoverflow.com/questions/45393923/python-tkinter-key-binding-to-all-subsequent-widgets, https://stackoverflow.com/questions/27802270/how-to-stop-a-function, https://stackoverflow.com/questions/3842155/is-there-a-way-to-make-the-tkinter-text-widget-read-only, https://stackoverflow.com/questions/20251161/tkinter-tclerror-image-pyimage3-doesnt-exist.
* [This tutorialspoint.com page](https://www.tutorialspoint.com/how-to-delete-tkinter-widgets-from-a-window#:~:text=We%20can%20delete%20widgets%20from,defining%20a%20function%20for%20it.), [this one](https://www.tutorialspoint.com/how-to-get-the-input-from-a-checkbox-in-python-tkinter#:~:text=Let%20us%20suppose%20that%20we,value%20of%20a%20particular%20widget.), and [this one](https://www.tutorialspoint.com/how-can-i-identify-when-a-button-is-released-in-tkinter)
* Paul Miskew for his [PYTHON 3 TKINTER - GUI ENTRY BIND KEY](https://youtu.be/JThKYGapGzU) video
* [This simplilearn.com page](https://www.simplilearn.com/tutorials/python-tutorial/python-typeof-function)
* [This realpython.com page](https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings)
* [This](https://www.youtube.com/watch?v=DCaKj3eIrro) video tutorial of LeMaster Tech on reading from a .txt file in Python
* [This flexiple.com page](https://flexiple.com/python/python-list-contains/)
* [This Runestone Academy page](https://runestone.academy/ns/books/published/fopp/SimplePythonData/UpdatingVariables.html#:~:text=In%20Python%20%2B%3D%20is%20used,or%20x%20%3D%20x%20%2B%201%20.)
* [This geeksforgeeks.org page](https://www.geeksforgeeks.org/append-extend-python/#:~:text=What%20is%20Append%20in%20Python,the%20end%20of%20a%20list.)
* [This digitalocean.com page](https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3)
* [This edureka.co page](https://www.edureka.co/community/33869/how-to-use-not-equal-operator-in-python#:~:text=You%20can%20use%20%22!%3D,are%20not%20equal%2C%20otherwise%20false%20.)
* [security.org](https://www.security.org/how-secure-is-my-password/)
* [This GitHub Docs page](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/approving-a-pull-request-with-required-reviews)
* [This video by plus 2 net](https://youtu.be/mSpLnnXeiIc)
* [This video from PyTutorials](https://youtu.be/DTnz8wA6wpw)
* [This video from Appficial](https://youtu.be/eszrY7w83q8)
