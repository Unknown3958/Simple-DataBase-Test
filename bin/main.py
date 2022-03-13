import os.path

print("Hello and welcome to UnknownDB!")
print("To get started type help for all commands.")

StoragePath = "../Storage/"

while True:
  cmd = input("UDB>")
  if cmd == "help":
    print("Welcome to the help menu!")
    print("cn: Creates a new file \nexit: Stop process \nopen: open an already existing file to edit. \nread: read the content of an existing file")
  if cmd == "cn":
    print("Provide a name for the file.")
    name = input("Name: ")
    file = open(StoragePath+''+name+".json","w")
    rawFile = open(StoragePath+''+name+"raw.Raw","w")
    rawFile1 = open(StoragePath+''+name+"raw.Raw","r")
    print("Variable Name.")
    varn = input("Var Name:")
    print("Varibale Value Type. (string/number)")
    vart = input('Type:')
    if vart == 'string':
      print("Variable value.")
      varv = input("Var Value:")
      content = '"'+varn+'": "'+varv+'"'
      rawFile.write(content)
      file.write("{\n "+content+"\n}")
      file.close()
      rawFile.close()
    if vart == 'number':
      print("Variable value.")
      varv = input("Var Value:")
      content = '"'+varn+'": '+varv
      rawFile.write(content)
      file.write("{\n "+content+"\n}")
      file.close()
      rawFile.close()
  if cmd == "createfile":
    print("Provide a name for the file.")
    name = input("Name: ")
    file = open(StoragePath+''+name+".json","w")
    rawFile = open(StoragePath+''+name+"raw.Raw","w")
    rawFile1 = open(StoragePath+''+name+"raw.Raw","r")
    print("Variable Name.")
    varn = input("Var Name:")
    print("Varibale Value Type. (string/number)")
    vart = input('Type:')
    if vart == 'string':
      print("Variable value.")
      varv = input("Var Value:")
      content = '"'+varn+'": "'+varv+'"'
      rawFile.write(content)
      file.write("{\n "+content+"\n}")
      file.close()
      rawFile.close()
    if vart == 'number':
      print("Variable value.")
      varv = input("Var Value:")
      content = '"'+varn+'": '+varv
      rawFile.write(content)
      file.write("{\n "+content+"\n}")
      file.close()
      rawFile.close()
  if cmd == "CreateFile":
    print("Provide a name for the file.")
    name = input("Name: ")
    file = open(StoragePath+''+name+".json","w")
    rawFile = open(StoragePath+''+name+"raw.Raw","w")
    rawFile1 = open(StoragePath+''+name+"raw.Raw","r")
    print("Variable Name.")
    varn = input("Var Name:")
    print("Varibale Value Type. (string/number)")
    vart = input('Type:')
    if vart == 'string':
      print("Variable value.")
      varv = input("Var Value:")
      content = '"'+varn+'": "'+varv+'"'
      rawFile.write(content)
      file.write("{\n "+content+"\n}")
      file.close()
      rawFile.close()
    if vart == 'number':
      print("Variable value.")
      varv = input("Var Value:")
      content = '"'+varn+'": '+varv
      rawFile.write(content)
      file.write("{\n "+content+"\n}")
      file.close()
      rawFile.close()
  if cmd == "Createfile":
    print("Provide a name for the file.")
    name = input("Name: ")
    file = open(StoragePath+''+name+".json","w")
    rawFile = open(StoragePath+''+name+"raw.Raw","w")
    rawFile1 = open(StoragePath+''+name+"raw.Raw","r")
    print("Variable Name.")
    varn = input("Var Name:")
    print("Varibale Value Type. (string/number)")
    vart = input('Type:')
    if vart == 'string':
      print("Variable value.")
      varv = input("Var Value:")
      content = '"'+varn+'": "'+varv+'"'
      rawFile.write(content)
      file.write("{\n "+content+"\n}")
      file.close()
      rawFile.close()
    if vart == 'number':
      print("Variable value.")
      varv = input("Var Value:")
      content = '"'+varn+'": '+varv
      rawFile.write(content)
      file.write("{\n "+content+"\n}")
      file.close()
      rawFile.close()
  if cmd == "cn ":
    print("Provide a name for the file.")
    name = input("Name: ")
    file = open(StoragePath+''+name+".json","w")
    rawFile = open(StoragePath+''+name+"raw.Raw","w")
    rawFile1 = open(StoragePath+''+name+"raw.Raw","r")
    print("Variable Name.")
    varn = input("Var Name:")
    print("Varibale Value Type. (string/number)")
    vart = input('Type:')
    if vart == 'string':
      print("Variable value.")
      varv = input("Var Value:")
      content = '"'+varn+'": "'+varv+'"'
      rawFile.write(content)
      file.write("{\n "+content+"\n}")
      file.close()
      rawFile.close()
    if vart == 'number':
      print("Variable value.")
      varv = input("Var Value:")
      content = '"'+varn+'": '+varv
      rawFile.write(content)
      file.write("{\n "+content+"\n}")
      file.close()
      rawFile.close()
  if cmd == "createfile ":
    print("Provide a name for the file.")
    name = input("Name: ")
    file = open(StoragePath+''+name+".json","w")
    rawFile = open(StoragePath+''+name+"raw.Raw","w")
    rawFile1 = open(StoragePath+''+name+"raw.Raw","r")
    print("Variable Name.")
    varn = input("Var Name:")
    print("Varibale Value Type. (string/number)")
    vart = input('Type:')
    if vart == 'string':
      print("Variable value.")
      varv = input("Var Value:")
      content = '"'+varn+'": "'+varv+'"'
      rawFile.write(content)
      file.write("{\n "+content+"\n}")
      file.close()
      rawFile.close()
    if vart == 'number':
      print("Variable value.")
      varv = input("Var Value:")
      content = '"'+varn+'": '+varv
      rawFile.write(content)
      file.write("{\n "+content+"\n}")
      file.close()
      rawFile.close()
  if cmd == "CreateFile ":
    print("Provide a name for the file.")
    name = input("Name: ")
    file = open(StoragePath+''+name+".json","w")
    rawFile = open(StoragePath+''+name+"raw.Raw","w")
    rawFile1 = open(StoragePath+''+name+"raw.Raw","r")
    print("Variable Name.")
    varn = input("Var Name:")
    print("Varibale Value Type. (string/number)")
    vart = input('Type:')
    if vart == 'string':
      print("Variable value.")
      varv = input("Var Value:")
      content = '"'+varn+'": "'+varv+'"'
      rawFile.write(content)
      file.write("{\n "+content+"\n}")
      file.close()
      rawFile.close()
    if vart == 'number':
      print("Variable value.")
      varv = input("Var Value:")
      content = '"'+varn+'": '+varv
      rawFile.write(content)
      file.write("{\n "+content+"\n}")
      file.close()
      rawFile.close()
  if cmd == "Createfile ":
    print("Provide a name for the file.")
    name = input("Name: ")
    file = open(StoragePath+''+name+".json","w")
    rawFile = open(StoragePath+''+name+"raw.Raw","w")
    rawFile1 = open(StoragePath+''+name+"raw.Raw","r")
    print("Variable Name.")
    varn = input("Var Name:")
    print("Varibale Value Type. (string/number)")
    vart = input('Type:')
    if vart == 'string':
      print("Variable value.")
      varv = input("Var Value:")
      content = '"'+varn+'": "'+varv+'"'
      rawFile.write(content)
      file.write("{\n "+content+"\n}")
      file.close()
      rawFile.close()
    if vart == 'number':
      print("Variable value.")
      varv = input("Var Value:")
      content = '"'+varn+'": '+varv
      rawFile.write(content)
      file.write("{\n "+content+"\n}")
      file.close()
      rawFile.close()
  if cmd == "open":
    print("Provide a file name.")
    name = input("Name: ")
    DoesExist = os.path.isfile(StoragePath+''+name+".json")
    if DoesExist == True:
      rawFile1 = open(StoragePath+''+name+"raw.Raw","r")
      previouscontent = rawFile1.read()
      print(previouscontent)
      rawFile1.close()
      file = open(StoragePath+''+name+".json","w")
      rawFile = open(StoragePath+''+name+"raw.Raw","w")
      print("Variable Name.")
      varn = input("Var Name:")
      print("Varibale Value Type. (string/number)")
      vart = input('Type:')
      if vart == 'string':
        print("Variable value.")
        varv = input("Var Value:")
        content = '"'+varn+'": "'+varv+'"'
        rawFile.write(previouscontent +",\n "+ content)
        file.write("{\n "+previouscontent+",\n "+content+"\n}")
        file.close()
        rawFile.close()
      if vart == 'number':
        print("Variable value.")
        varv = input("Var Value:")
        content = '"'+varn+'": '+varv
        rawFile.write(previouscontent +",\n "+ content)
        file.write("{\n "+previouscontent+",\n "+content+"\n}")
        file.close()
        rawFile.close()
    else:
      print('File Does not exist')
      print('Create a new file by typing cn.')
  if cmd == "Open":
    print("Provide a file name.")
    name = input("Name: ")
    DoesExist = os.path.isfile(StoragePath+''+name+".json")
    if DoesExist == True:
      rawFile1 = open(StoragePath+''+name+"raw.Raw","r")
      previouscontent = rawFile1.read()
      print(previouscontent)
      rawFile1.close()
      file = open(StoragePath+''+name+".json","w")
      rawFile = open(StoragePath+''+name+"raw.Raw","w")
      print("Variable Name.")
      varn = input("Var Name:")
      print("Varibale Value Type. (string/number)")
      vart = input('Type:')
      if vart == 'string':
        print("Variable value.")
        varv = input("Var Value:")
        content = '"'+varn+'": "'+varv+'"'
        rawFile.write(previouscontent +",\n "+ content)
        file.write("{\n "+previouscontent+",\n "+content+"\n}")
        file.close()
        rawFile.close()
      if vart == 'number':
        print("Variable value.")
        varv = input("Var Value:")
        content = '"'+varn+'": '+varv
        rawFile.write(previouscontent +",\n "+ content)
        file.write("{\n "+previouscontent+",\n "+content+"\n}")
        file.close()
        rawFile.close()
    else:
      print('File Does not exist')
      print('Create a new file by typing cn.')
  if cmd == "open ":
    print("Provide a file name.")
    name = input("Name: ")
    DoesExist = os.path.isfile(StoragePath+''+name+".json")
    if DoesExist == True:
      rawFile1 = open(StoragePath+''+name+"raw.Raw","r")
      previouscontent = rawFile1.read()
      print(previouscontent)
      rawFile1.close()
      file = open(StoragePath+''+name+".json","w")
      rawFile = open(StoragePath+''+name+"raw.Raw","w")
      print("Variable Name.")
      varn = input("Var Name:")
      print("Varibale Value Type. (string/number)")
      vart = input('Type:')
      if vart == 'string':
        print("Variable value.")
        varv = input("Var Value:")
        content = '"'+varn+'": "'+varv+'"'
        rawFile.write(previouscontent +",\n "+ content)
        file.write("{\n "+previouscontent+",\n "+content+"\n}")
        file.close()
        rawFile.close()
      if vart == 'number':
        print("Variable value.")
        varv = input("Var Value:")
        content = '"'+varn+'": '+varv
        rawFile.write(previouscontent +",\n "+ content)
        file.write("{\n "+previouscontent+",\n "+content+"\n}")
        file.close()
        rawFile.close()
    else:
      print('File Does not exist')
      print('Create a new file by typing cn.')
  if cmd == "Open ":
    print("Provide a file name.")
    name = input("Name: ")
    DoesExist = os.path.isfile(StoragePath+''+name+".json")
    if DoesExist == True:
      rawFile1 = open(StoragePath+''+name+"raw.Raw","r")
      previouscontent = rawFile1.read()
      print(previouscontent)
      rawFile1.close()
      file = open(StoragePath+''+name+".json","w")
      rawFile = open(StoragePath+''+name+"raw.Raw","w")
      print("Variable Name.")
      varn = input("Var Name:")
      print("Varibale Value Type. (string/number)")
      vart = input('Type:')
      if vart == 'string':
        print("Variable value.")
        varv = input("Var Value:")
        content = '"'+varn+'": "'+varv+'"'
        rawFile.write(previouscontent +",\n "+ content)
        file.write("{\n "+previouscontent+",\n "+content+"\n}")
        file.close()
        rawFile.close()
      if vart == 'number':
        print("Variable value.")
        varv = input("Var Value:")
        content = '"'+varn+'": '+varv
        rawFile.write(previouscontent +",\n "+ content)
        file.write("{\n "+previouscontent+",\n "+content+"\n}")
        file.close()
        rawFile.close()
    else:
      print('File Does not exist')
      print('Create a new file by typing cn.')
  if cmd == 'read':
    print("Provide a file name.")
    name = input("Name: ")
    DoesExist = os.path.isfile(StoragePath+''+name+".json")
    if DoesExist == True:
      file = open(StoragePath+''+name+".json","r")
      print(file.read())
  if cmd == "exit":
    print('Exited')
    break