**I.PROJECT OVERVIEW**

The EcoSeas app is designed to inspire and educate people about the incredible world beneath the waves while empowering them to help protect it. Our oceans face serious challenges like pollution, climate change, and overfishing, and this app aims to make a difference by bringing awareness to these issues. Through interactive features, beautiful visuals, and easy-to-understand information, EcoSeas helps users learn about marine species, their habitats, and the vital roles they play in our planet’s health. It also provides simple, actionable tips for sustainable living, showing how small changes can have a big impact. At its heart, EcoSeas is about connecting people with the ocean, encouraging everyone to play a part in preserving its beauty and biodiversity for generations to come.



**II.PYTHON CONCEPTS AND LIBRARIES**

**II.1 Python Tkinter**

**1.Master(Root Window)** the main container where everything else will be placed.

**2.Widgets**

  **A.Label:** Displays text or images

  **B.Frame:** Organizes other widgets.
  
  **C.Button:** A clickable button that triggers actions.
  
  **D.Canvas:** For drawing or placing complex layouts.
  
  **E.Scrollbar:** For scrolling content.
  
**3.Managing the Layout of widgets**

  **A..pack():** Places widgets in a vertical or horizontal line.

  **B..place():** Allows you to position widgets anywhere on the screen.

  **C..grid():** Organizes widgets in a grid-like structure, which is helpful for complex forms or arrangements.

4.**Ttk Module** enhances the look of tkinter widgets. It offers widgets like Notebook, which is used for creating tabbed interfaces in the application.

5.**Pillow Library** The developer use Pillow library to be able input images in the application.

6.**Application Structure**

  **A.Constructor** (__init__):

    The constructor initializes the main window, sets up the title, and creates the tabs 	for different sections like the marine life library, environmental threats, and more.

  **B.Tabs:**

    The app uses a tabbed interface (ttk.Notebook), where each tab has its own 	content. (Marine life library, Environmental Threats, Conservation Tips, 	Interactive Learning).

  **C.Scrollable Frames:**
	
     Some sections (like the Marine Life Library tab) may have a lot of information, so 	the content is made scrollable using a Canvas widget combined with a Scrollbar.

  **D.Dynamic Content:**
	
     Based on user selections (like choosing a marine species), the app dynamically 	updates the content, showing related images and information.

 **E.Interactive Features:**
 
	    The Learning Tab contains interactive elements like quizzes.


**II.2 MySQL**

1.**Connecting to the Database** The script starts by connecting to a MySQL database called "Ecoseas" using the mysql.connector library. It connects to the local MySQL server as the root user with no password.

2.**Creating a Cursor** Once connected, the script creates a cursor. It helps to execute SQL queries and fetch results from the database.

3.**Inserting Data (Commented Out)**
  
  **Category:** This would insert data like "Mammals", "Plants", and "Ocean Fishes".
  
  **Species:** This would insert information about various species.
  
  **Threats:** This would insert different environmental threats like "Plastic Pollution" and "Climate Change".
 
  **Conservation Tips:** This would insert helpful tips, such as "Reduce Plastic Usage" and "Support Sustainable Seafood".
  
  **Quizzes**: This would insert quiz data with questions about the species.

4.**Fetching Data** The script then retrieves all the data from each of the five tables:
  
  It runs a SELECT * query on each table.
  
  For each table, it prints the results. This way, you can see all the records in the Category, Species, Threats, Conservation Tips, and Quizzes tables.

5.**Closing the Connection** Once the data is printed, the script will close.



**III.SUSTAINABLE DEVELOPMENT GOALS**

**EcoSeas** is an application designed to actively contribute to global sustainability by focusing on key Sustainable Development Goals (SDGs). One of the primary goals it supports is **SDG 14: Life Below Water**, which aims to protect and sustainably manage oceans, seas, and marine resources. EcoSeas educates users about marine life through detailed species profiles and highlights the threats facing oceans, such as plastic pollution, overfishing, and climate change. By encouraging sustainable behaviors like reducing plastic use and supporting sustainable fishing, the app empowers users to take actionable steps to protect marine ecosystems.

EcoSeas also aligns with **SDG 12: Responsible Consumption and Production**, promoting sustainable consumption patterns. The app provides users with practical advice on making eco-friendly choices, such as reducing single-use plastics and opting for businesses with sustainable practices. This directly contributes to a more responsible consumption model, encouraging users to minimize their environmental impact. Furthermore, the app supports **SDG 13: Climate Action** by educating users on how climate change affects marine life and urging them to reduce their carbon footprints to mitigate its impacts.

In addition to promoting environmental action, EcoSeas supports **SDG 4: Quality Education** by providing interactive learning experiences. The app offers fun facts, quizzes, and detailed educational content on marine life, making learning accessible. By raising awareness about environmental issues and their consequences, EcoSeas helps foster a sense of responsibility toward protecting the planet.

EcoSeas also contributes to **SDG 15: Life on Land**, emphasizing the interconnectedness of land and marine ecosystems. By highlighting how protecting the oceans contributes to the health of the entire planet, the app encourages users to take a holistic approach to environmental conservation.

In conclusion, EcoSeas is a powerful tool for promoting sustainability by aligning with multiple SDGs. Through education, and actionable tips, the app empowers users to make informed decisions that protect the environment and ensure a sustainable future for generations to come.



**IV.PROGRAM/SYSTEM INSTRUCTIONS**

1.**Launch the Application:**

  Just run the Python script to open EcoSeas. You’ll see the main window appear, displaying the EcoSeas title at the top.

2.**Explore Marine Life:**

  Go to the **“Marine Life Library”** tab.
  
  Start by choosing a category from the dropdown (such as Mammals, Ocean Fishes, Plants, or Others). Once you pick a category, the list of related species will appear.
  
  Select any species from the list, and you’ll see:
  
    A detailed description of that species.
    
    If available, a photo of the species will also show up.
    
3.**Learn About Environmental Threats:**

  Next, head to the **“Environmental Threats”** tab.
  
  This section lists some of the biggest dangers to marine life, like plastic pollution, climate change, and overfishing. Each threat comes with an explanation of how it harms the ocean and its inhabitants.

4.**Discover Conservation Tips:**
  
  Click on the **“Conservation Tips”** tab for practical advice on how you can help protect the oceans.  
  
  Tips include things like using less plastic, supporting sustainable seafood, and taking part in beach cleanups. These simple actions can make a big difference in preserving marine life.

5.**Interactive Learning (Take a Quiz!):**
  
  In the **“Interactive Learning”** tab, you’ll find a quiz about marine life. Test your knowledge by answering multiple-choice questions.
  
  After you complete the quiz, click the **“Show Results”** button to see how well you did and learn which answers you got right.

6.**Navigating the App:**
  
  You can easily switch between tabs to explore different topics.
  
  If a section is long (like the threats or species library), use the scrollbars to scroll through.
  
  If you want to exit, Just click the **"Close"** button in the quiz window or close the main app window to exit.
