import random
import markdown2

from . import util
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Index
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Search for Entry
def search(request):
    query = request.GET.get("q", "")
    entries = util.list_entries()
    suggestions = [] # List of substrings
    for entry in entries:
        # Find & load exact match
        if query.casefold() == entry.casefold():      
            return render(request, "encyclopedia/entry.html", {
                "entry": markdown2.markdown(util.get_entry(query)),
                "title": entry
            })
        
        # Look for matching substrings
        if query.casefold() in entry.casefold() or entry.casefold() in query.casefold():
            suggestions.append(entry)
    
    # Load 'no exact match' / 'no match' page
    return render(request, "encyclopedia/search_results.html", {
        "entries": suggestions,
        "query": query
    })

# load entry
def show_entry(request, query):
    entries = util.list_entries()  
    for entry in entries:
        if entry.casefold() == query.casefold():
            return render(request, "encyclopedia/entry.html", {
                "entry": markdown2.markdown(util.get_entry(query)),
                "title": entry
            })      
    return render(request, "encyclopedia/errorpage.html")

# New Entry Form
class NewEntry(forms.Form):
    form_title = forms.CharField(widget=forms.TextInput(attrs={'size':60}), label="Title of Entry:")
    form_content = forms.CharField(widget=forms.Textarea, label="Content of Entry:")

# Add New Entry
def new_entry(request):
    if request.method == "POST":
        form = NewEntry(request.POST)
        
        # Check if form data is valid (server-side)
        if form.is_valid():
            filename = form.cleaned_data["form_title"]
            content = form.cleaned_data["form_content"]            
            entries = util.list_entries()
            
            # Check if entry already existing
            for entry in entries:
                if entry.casefold() == filename.casefold():
                    return render(request, "encyclopedia/new_entry.html", {
                        "error": "Error: An entry with this name already exists!",                        
                        "form": form
                    })

            # Add new_entry to entries-folder
            util.save_entry(filename, content)

            # Render new entry
            return render(request, "encyclopedia/entry.html", {
                "entry": markdown2.markdown(util.get_entry(filename)),
                "title": filename
            })    

        else:
            # invalid form: re-render page with existing info
            return render(request, "encyclopedia/new_entry.html", {
                "form": form
            })
            
    # method = GET
    return render(request, "encyclopedia/new_entry.html", {
        "form": NewEntry()
    })

# Edit Entry Form
class ModEntry(forms.Form):
    form_content = forms.CharField(widget=forms.Textarea, label="Content of Entry: ")

# Edit Existing Entry
def edit_entry(request, title):
    if request.method == "POST":
        form = ModEntry(request.POST)
        
        # Check if form data is valid (server-side)
        if form.is_valid():
            filename = title
            content = form.cleaned_data["form_content"]            
            
            # Add edited entry to entries-folder
            util.save_entry(filename, content)

            # Render edited entry
            return render(request, "encyclopedia/entry.html", {
                "entry": markdown2.markdown(util.get_entry(filename)),
                "title": filename
            })    

        else:
            # invalid form: re-render page with existing info
            return render(request, "encyclopedia/new_entry.html", {
                "form": form
            })

    # method = GET    
    return render(request, "encyclopedia/edit_entry.html", {
        "title": title,         
        "form": ModEntry(initial={"form_content": util.get_entry(title)})
    })

# Load Random Entry
def random_entry(request):
    entries = util.list_entries()
    entry = random.choice(entries)
    return HttpResponseRedirect(f"wiki/{entry}")
