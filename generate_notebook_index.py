# python3 program that reads the notebook index text file and generates a nicely formatted text for printing out
# ebrahim

class NotebookEntry:
  def __init__(self, page_number, description):
    self.page_number = page_number
    self.description = description


class Notebook:
  def __init__(self, name, description=''):
    self.name = name
    self.description = description
    self.entries = []
  
  def add_entry(self, notebook_entry):
    self.entries.append(notebook_entry)

  def __iter__(self):
    return self.entries.__iter__()



# Populate list of notebooks by parsing file
notebooks = []
f = open("notebook_index.txt")
for line in f.readlines():
  line = line.strip()
  if not line: continue
  components = [component.strip() for component in line.split(':')]
  assert(len(components)>=1 and len(components)<=2) # Every line should have at most 2 components: a header, and then possible a ':' with info after it
  if len(components)==1 : components.append('')

  if components[0][0]=='N' : # If notebook number heading
    notebooks.append(Notebook(*components))

  else: # Otherwise we have a notebook entry
    assert(len(notebooks)>0)  # There needs to have been a notebook number heading before any notebook entries show up
    notebooks[-1].add_entry(NotebookEntry(*components))
f.close()


# Sort each notebook's entries by page number
for notebook in notebooks:
  notebook.entries.sort(key = lambda entry : int(entry.page_number))





for notebook in notebooks:
  print(notebook.name)
  if notebook.description:
    print('    ',notebook.description)

  print()


  # Determine the width of the longest description:
  description_width = max(len(entry.description) for entry in notebook)
  format_string = "{:<"+str(description_width+2)+"} {}"

  for entry in notebook:
    print(format_string.format(entry.description,entry.page_number))

  print('\n\n')



