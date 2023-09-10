from src import refresh
import time
import json

'''
ok i am so confused on what the goal is so im gonna try to figure it out now:
  the slides that i want:
    need the times for a class? here are time!
    who are you looking for. we will tell you what you need to know
  slides i might want:
    raw information. all of the information.
  how it's formatted for the file:
    problem is that you're gonna have to repeat data (names or classes)
    i would concentrate on sorting the names first, then get the times from the names,
      then get the classes from the times.
    hopefully something clicks next time i work on this

    hey i think something clicked you just use a json list:
      [
        {
          name: "",
          email: "",
          classes: [],
          days: BITMAP???, # 6 days max 
          times: [],
          isOnline: bool
        }, {repeat}
      ]
    i hate this because it's like "i'm going to write every object as follows" but does anyone really want to do that?? come on man.
    im jUST REWRITING EVERYTHING THIS IS SO ANNOYING

    ALTERNATIVELY
    every line in the file has all the info about the person in order, separated by some separator character like | (probably a bad idea)

OH!
there should be a script that edits a database that modifies a person's schedule for a day. what's the framework looking like for that??
animal boinking
'''

# writes to named file to be read by c parser
# firstname, lastname, email, times, classes
# is there like a distinction to online? are there solely online tutors?

def hour24(t):
  # converts xxMM into 24 hour number. if any time slot has a minute section i will die
  split_index = 1
  if t[1].isdigit():
    # 2 digit beginning
    split_index += 1
  num = int(t[0:split_index])
  median = t[split_index:]
  if median == 'PM':
    num += 12
  if num % 12 == 0:
    num -= 12
  return num * 100

def hourminute24(t):
  # converts xx:xxMM into a 24 hour number
  hour, rest = t.split(':')
  minute = int(rest[0:2])
  hour = int(hour)

  return hour24(hour+rest[2:]) + minute

def person_info(values, file):
  ret = []
  for val in values:
    dret = {
      "name": '',
      "email": '',
      "sections": [],
      "classes": [],
      'isOnline': False
    }
    dret['name'] = f"{val[1]} {val[0]}" # goes last name first name on sheet
    dret['email'] = val[2]
    for SECTION in val[3].split(", "):
      sect_ret = {
        "date": '', #character
        "time": [] #start,end
      }
      if (len(SECTION.split(' ')) > 2):
        dret['isOnline'] = True

      d , t = SECTION.split(" ")[0:2]
      if d == "Th":
        d = "R"
      d = d[0] # get first character
      sect_ret['date'] = d
      for TIME in t.split('-'):
        if (':' in TIME):
          TIME = hourminute24(TIME)
        else:
          TIME = hour24(TIME)
        sect_ret["time"].append(TIME)
      dret['sections'].append(sect_ret)
    dret['classes'] = val[4]

    ret.append(dret)
  json.dump(ret, file)

def main():
  '''
  TODO: call refresh every 24 hours, and write output to file
  '''
  SPREADSHEET_ID = '1yixBkRbiC_Af2G9RhysgC_t0WeUp_ah6FN-fi88bnKQ'
  RANGE = "D3:H26"
  FILE_NAME = "data.json"

  while True:
    values = refresh.refresh(SPREADSHEET_ID, RANGE)
    st = time.localtime()
    printed_time = f"{st.tm_year}-{st.tm_mon:02}-{st.tm_mday:02} {st.tm_hour:02}:{st.tm_min:02}"
    if not values:
      print("%s: Refresh retreival failed!" % printed_time) 
      continue
    print("%s: Updating file with schedule" % printed_time)
    print(values)
    with open(FILE_NAME, 'w') as file:
      person_info(values, file)
    return values
    time.sleep(24*60*60) # die

if __name__ == "__main__":
  main()
