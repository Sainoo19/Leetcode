import datetime


class Document(object):
    ID = 0

    def __init__(self):
        Document.ID += 1
        self.DocumentID = Document.ID
        self.fileName = 'Document' + str(Document.ID)
        self.createDate = datetime.datetime.now()
        self.lastModifiedDate = None
        self.content = None
        self.modifiedDate = None

    def __str__(self):
        return str(self.fileName) + ' ' + str(self.createDate) + ' ' + str(self.modifiedDate)

    def inputContent(self):
        pass

    def save(self):
        pass

    def saveAs(self, newName):
        pass

    def open(self):
        pass


class Textpad(Document):
    def __init__(self):
      Document.__init__(self)
      self.words = 0
      self.size = 0

    def getWords(self):
      self.words = len(self.content.split())
      return self.words

    def getChars(self):
      self.size = len(self.content)
      return self.size

    def inputContent(self):
      self.content = str(input('Nhap thong tin: '))

    def save(self):
      if self.content == None:
        self.content = ''
      self.lastModifiedDate = datetime.datetime.now()
      file = open(self.fileName, 'a')
      file.write(self.content)
      file.close()

    def saveAs(self, newName):
      self.lastModifiedDate = datetime.datetime.now()
      file = open(newName, 'a')
      file.write(self.content)
      file.close()

    def open(self):
      return str(self.fileName) + '\n' + str(self.content) + '\nNgay tao: ' + str(self.createDate) + '\nNgay cap nhat cuoi: ' + str(self.lastModifiedDate) + '\nSo tu: ' + str(self.getWords()) + '\nSo ky tu: ' + str(self.getChars())


txt = Textpad()
txt.inputContent()  
txt.save()
txt.saveAs('Document2')
print(txt.open())