
from browser import document, html, window, highlight, alert
    
# Check Storage Functions
try:
    storage = window.localStorage
    storage.setItem("x", "x")
    storage.removeItem("x")
except:
    storage = None

if storage is None:
    cur_lan = ".en"
else:
    cur_lan = storage['lan']

# create first menu entry (intro page)
def intro(ev):
    global current
    if current is not None:
        document[current].style.display = "none"
        document <= document[current]
        document["a"+current].classList.remove("selected")
    exercise_id = "intro"
    exercise = document[exercise_id]
    ev.target.parent.classList.add("selected")
    document["panel"].clear()
    document["panel"] <= exercise
    document[exercise_id].style.display="block"
    current = exercise_id

anchor = html.A("<span class='lan en'>Foreword</span><span class='lan cn'>前言</span>", Class="menu selected", href="#", id="aintro")
anchor.bind("click", intro)

document["menu"] <= html.LI(anchor)
current = "intro"

def load_exercise(ev):
    global current
    # remove dialogs
    for dialog in document.select(".brython-dialog-main"):
        dialog.remove()
    if current is not None:
        document[current].style.display = "none"
        document <= document[current]
        document["a"+current].classList.remove("selected")
    exercise_id = ev.target.parent.num
    exercise = document[exercise_id]
    ev.target.parent.classList.add("selected")
    document["panel"].clear()
    document["panel"] <= exercise
    exercise.style.display="block"
    script = exercise.get(selector="script")[0]
    src = script.text
    while src.startswith("\n"):
        src = src[1:]
    indent = 0
    while src[indent] == ' ':
        indent += 1
    src = "\n".join(line[indent:] for line in src.split("\n"))
    src = highlight.highlight(src)
    code_elt = exercise.get(selector="pre")
    if code_elt:
        code_elt[0].html = src.html
    else:
        exercise <= src
    current = exercise_id


for exercise in document.get(selector=".exercise"):
    # add the Python source inside the exercise

    # create a menu entry
    question_en = exercise.get(selector="question")[0]
    question_cn = exercise.get(selector="question")[1]
    question = "<span class='lan en'>"+question_en.text+"</span><span class='lan cn'>"+question_cn.text+"</span>"
    anchor = html.A(question, Class="menu", href="#", id="a"+exercise.id)
    anchor.num = exercise.id

    anchor.bind("click", load_exercise)
    document["menu"] <= html.LI(anchor)

    # hide the element
    exercise.style.display = "none"



# Language Script Start
lan_dict = {
    "English":".en",
    "中文":".cn"
}

if storage is None:
    cur_lan = ".en"
else:
    cur_lan = storage['lan']

elements_lan = document.select(".lan")
elements_en = document.select(".en")
elements_cn = document.select(".cn")

def show_lan(lan='.en'):
    for element_lan in elements_lan:
        element_lan.style.display = "none"
    for element_select in document.select(lan):
        element_select .style.display = "inherit"

if storage is None:
    show_lan()
else:
    lan = '.en' if ('lan' not in storage or storage['lan'] not in lan_dict.values()) else storage['lan']
    language = [k for k,v in lan_dict.items() if v==lan]
    show_lan(lan)

def show(ev):
    global cur_lan
    cur_lan = ev.target.textContent
    if storage is not None:
        if 'lan' in storage and storage['lan'] == lan_dict[cur_lan]:
            return
        storage['lan'] = lan_dict[cur_lan]
    show_lan(storage['lan'])
    document['cur_lan'].innerHTML = cur_lan

menu_lan = html.SPAN("English" if storage is None or 'lan' not in storage else language, id="cur_lan")
menu_lan.setAttribute('Class','language')
div_lan = document.createElement("div")
div_lan.setAttribute('id','language_options')
for lan_name in lan_dict:
    option_lan = document.createElement("p")
    txt = document.createTextNode(lan_name)
    option_lan.appendChild(txt)
    option_lan.bind("click", show)
    div_lan <= option_lan

document['div_language'] <= menu_lan
document['div_language'] <= div_lan

# Language Script End