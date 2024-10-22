from bs4 import BeautifulSoup

def create_project_dict():
    # Read the local HTML file
    html = ''
    with open('./fixtures/kickstarter.html') as file:
        html = file.read()
    
    # Create BeautifulSoup object to parse HTML
    kickstarter = BeautifulSoup(html, 'html.parser')
    
    # Initialize projects dictionary
    projects = {}
    
    # Iterate through each project
    for project in kickstarter.select("li.project.grid_4"):
        # Extract project title to use as dictionary key
        title = project.select("h2.bbcard_name strong a")[0].text
        
        # Create nested dictionary for project details
        projects[title] = {
            'image_link': project.select("div.project-thumbnail a img")[0]['src'],
            'description': project.select("p.bbcard_blurb")[0].text,
            'location': project.select("ul.project-meta span.location-name")[0].text,
            'percent_funded': project.select("ul.project-stats li.first.funded strong")[0].text.replace("%","")
        }
    
    return projects