from src import refresh
import time
'''
ok i am so confused on what the goal is so im gonna try to figure it out now:
  the slides that i want:
    who's tutoring today? what times? what classes?
    need the times for a class? here are time!
    did you meet a tutor you like? here are the people's times.
  slides i might want:
    raw information. all of the information.
  how it's formatted for the file:
    problem is that you're gonna have to repeat data (names or classes)
    i would concentrate on sorting the names first, then get the times from the names,
      then get the classes from the times.
    hopefully something clicks next time i work on this

'''
# writes to named file to be read by c parser
# firstname, lastname, email, times, classes
# is there like a distinction to online? are there solely online tutors?
def write_class_time(values, file):


def write_time_class(values, file):
  

def main():
  '''
  TODO: call refresh every 24 hours, and write output to file
  '''
  SPREADSHEET_ID = '1yixBkRbiC_Af2G9RhysgC_t0WeUp_ah6FN-fi88bnKQ'
  RANGE = "D3:H26"

  while True:
    values = refresh.refresh(SPREADSHEET_ID, RANGE)
    st = time.localtime()
    printed_time = f"{st.tm_year}-{st.tm_mon:02}-{st.tm_mday:02} {st.tm_hour:02}:{st.tm_min:02}"
    print("%s: Updating file with schedule" % printed_time)
    print(values)
    time.sleep(24*60*60) # die

if __name__ == "__main__":
  main()
