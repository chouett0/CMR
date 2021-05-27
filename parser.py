import re
import os
import sys


def fixSentence(content):
   fix_data = {
      "=3D": "="
   }

   c = []
   for line in content:
      if (len(line) > 2 ):
         if ( line[-2] is '=' ):
            line = line[:-2]
      for target, replace in fix_data.items():
         if ( target in line ):
            line = line.replace(target, replace)

      c.append(line)

   return c


def fixEncode(c):
   for i in range(0, len(c)):
      if ( '?$' in c[i] ):
         data = c[i].split('?')

         for j in range(0, len(data)):
            try:
               if ( len(data[j]) > 2 and data[j][-1] is '$' ):
                  data[j] = data[j][:-1]
               a=b'\x1b'+data[j].encode('utf-8')
               data[j] = a.decode(encoding='iso2022-jp')
            except Exception as e:
#               print("[ * ] ", end='')
#               print(c[i], end='')
#               print(e)
               print("[ * ] {} : {}".format(c[i], e))
#               pass
         c[i] = ''.join(data)

   return c


def parseForHTML(c):
   content = fixEncode( fixSentence(c) )
#   content = fixSentence( fixEncode(c) )
   return content

def main():

   if ( not os.path.exists(sys.argv[1]) ):
      print("[ ! ] Cannot read file.")
      sys.exit(1)
   else:
      target_file = sys.argv[1]

   with open(target_file, "r") as fd:
      raw_content = fd.readlines()
   
   content = parseForHTML(raw_content)

   with open("./output.txt", "w") as fd:
      for line in content:
        fd.writelines(line)

   

if __name__ == "__main__":
   main()
