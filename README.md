# Passwordsy
RETIRED REPOSITORY

A program that can generate a secure password of up to 100 characters, extract securely selected words from the diceware wordlist, generate a password from a sentence, and check for vulnerabilities in a given password.

## Known limitations
Avoid using a keyboard layout that types diacritics through a shortcut (such as the Romanian Programmers, where ș is ALT + S, and ț is ALT + T). The diacritic might turn into its non-diacritic counterpart (Ț into T) or into a question mark. I recommend using a keyboard layout that types diacritics directly (such as the Romanian Standard, where ; types ș and ' types ț).

## Getting started
To use Passwordsy, you must get the program itself on your machine. To do this, you have 3 choices: cloning it through Git, opening it with GitHub Desktop, or downloading it as a ZIP. The following tutorial describes installing Passwordsy by cloning the repository with Git.

### Prerequisites
- Git from git-scm.com
- Python from python.org (make sure to tick 'Add Python to PATH' during the installation process)
- The following modules: PIL, Clipboard, Pynput, CustomTkinter. They are found in the requirements.txt file.

### Installation
- Open Git Bash
- Use cd (change directory) to move to the location you want the repository to be cloned in. For example, if you want the repository to be cloned in the 'projects' folder on Desktop, type 'cd Desktop/projects/' in the terminal.
- Once you are in the desired folder, type 'git clone https://github.com/IceTheDev2/Passwordsy.git'.
- Type 'cd Passwordsy' and then 'pip install -r requirements.txt' to move into the main directory of the repository and to install all the required dependencies.
- Type 'cd code' to the navigate to the file containing main.py.
- Type 'python main.py' to run the program

## Usage
### Generate 4 secure strings of 4 to 100 characters, with custom character sets
<a data-flickr-embed="true" href="https://www.flickr.com/photos/197764307@N08/52775455345/in/dateposted-public/" title="46"><img src="https://live.staticflickr.com/65535/52775455345_dbc840fa34_o.png"></a>

### Check a given password's strength and provide tips to improve its security
<a data-flickr-embed="true" href="https://www.flickr.com/photos/197764307@N08/52775046031/in/dateposted-public/" title="47"><img src="https://live.staticflickr.com/65535/52775046031_b94f4b19fb_o.png">

### Get up to 35 copyable words and their paired numbers from the diceware wordlist
<a data-flickr-embed="true" href="https://www.flickr.com/photos/197764307@N08/52775063281/in/dateposted-public/" title="48"><img src="https://live.staticflickr.com/65535/52775063281_c4485569e6_o.png"></a>

### Generate a memorable password from a given sentence and provide tips to improve it
<a data-flickr-embed="true" href="https://www.flickr.com/photos/197764307@N08/52775549023/in/dateposted-public/" title="49"><img src="https://live.staticflickr.com/65535/52775549023_9458605963_o.png" alt="49"/></a>

## Contributing
I'd love to hear your suggestions on how I can improve my first project!  
You can fork the project to play around with it and create a pull request to submit your suggestions. You can also open an issue to tell me about any problems my code might have.

## License
This repository is licensed under the MIT license. In short, you must include the exact copy of this project's license in your end-user application. Read LICENSE for more information.

If you decide to use portions of my software, it would be appreciated if you include an attribution in the final application, mentioning the name of software and its contributors, as well as the section(s) in which it was used.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Acknowledgements
* The [r/Python](https://www.reddit.com/r/Python/), [r/learnprogramming](https://www.reddit.com/r/learnprogramming/) and [r/learnpython](https://www.reddit.com/r/learnpython/) communities on Reddit for providing me with great tips and suggestions
* The GitHub contributors to this project, [dwaffle](https://github.com/dwaffle), [christopher-chandler](https://trello.com/c/f72vJsYk/50-https-githubcom-christopher-chandler), and [MartinMerkli](https://github.com/MartinMerkli)
* [u/creedxender](https://www.reddit.com/user/creedxender/) for suggesting a 'Secret string of letters, numbers, and/or symbols'.
* [u/infra_d3ad](https://www.reddit.com/user/infra_d3ad/) for suggesting using diceware.
* [u/modernknight87](https://www.reddit.com/user/modernknight87/) for suggesting 'The user input a sentence of their own choosing, takes the first letter of every word, and any numbers or symbols, and combines those as the produced password'.
* [u/ekchew](https://www.reddit.com/user/ekchew/) for taking the time to rework the check_password_complexity function.
* [u/Diapolo10](https://www.reddit.com/user/Diapolo10/) for taking the time to analyze large parts of my code and provide me with great suggestions on improving readability and preventing errors.
* The [codemy.com Youtube channel](https://www.youtube.com/@Codemycom) for their great Tkinter tutorials, such as: [this one on keyboard event binding](https://youtu.be/GLnNPjL1U2g), [this one on cursor positions](https://youtu.be/Z4zePg2M5H8), [this one on Tkinter menus](https://youtu.be/KRuUtNxOb_k), [this one on message boxes](https://youtu.be/S3AaSwpb5GE).
* The [SecLists repository](https://github.com/danielmiessler/SecLists) of danielmiessler, used here for the 100,000 most common passwords.
* The [Diceware-Password-Generator repository](https://github.com/sameera-madushan/Diceware-Password-Generator) of sameera-madushan, used here to generate for a unique password-generation mode.
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
