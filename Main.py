import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk



class EcoSeasApp:
    def __init__(self, master):
        self.master = master
        self.master.title("EcoSeas")
        self.master.geometry("1100x600")
        self.master.resizable(0, 0)  # to not resize

        # Main container
        self.main_frame = tk.Frame(master, bg="#293241")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Title Label
        self.title_label = tk.Label(
            self.main_frame, text="EcoSeas",
            font=("Helvetica", 40, "bold"), bg="#293241", fg="#98c1d9"
        )
        self.title_label.pack(pady=40)

        # Tabs
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Tabs for each section
        self.create_tabs()

    def create_tabs(self):
        # Marine Life Library Tab
        self.library_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.library_tab, text="Marine Life Library")
        self.create_library_tab()

        # Environmental Threats Tab
        self.threats_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.threats_tab, text="Environmental Threats")
        self.create_threats_tab()

        # Conservation Tips Tab
        self.tips_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.tips_tab, text="Conservation Tips")
        self.create_tips_tab()

        # Interactive Learning Tab
        self.learning_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.learning_tab, text="Interactive Learning")
        self.create_learning_tab()

    def create_scrollable_frame(self, parent):
        canvas = tk.Canvas(parent)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        # Configure canvas scrolling
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Layout canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        return scrollable_frame
        
    def create_library_tab(self):
        top_frame = tk.Frame(self.library_tab, bg="#8d99ae")
        top_frame.pack(fill=tk.X, pady=10)

        description = tk.Label(
            top_frame,
            text="Explore the rich biodiversity of marine life. Select a category and species to learn more:",
            font=("Helvetica", 12),
            bg="#8d99ae",
            wraplength=900,
            justify="left"
        )
        description.pack(pady=10)

        # Define categories and species
        self.categories = {
            "Mammals": ["Dolphin", "Whale", "Seals", "Sea Lions", "Sea Otters", "Manatees"],
            "Plants": ["Phytoplankton", "Seagrasses", "Algae", "Kelp", "Sargassum"],
            "Ocean Fishes": ["Shark", "Seahorse", "Bluefin Tuna", "Eel"],
            "Others": ["Octopus", "Crabs", "Lobster", "Shrimp"]
        }

        # Dropdown for categories
        self.category_var = tk.StringVar()
        self.category_var.set("Select a category")
        dropdown_frame = tk.Frame(top_frame, bg="#8d99ae")
        dropdown_frame.pack(pady=10)

        category_dropdown = ttk.OptionMenu(
            dropdown_frame, self.category_var, "Select a category", *self.categories.keys(), command=self.update_species_dropdown
        )
        category_dropdown.pack(side="left", padx=10)

        # Dropdown for species (initially empty)
        self.species_var = tk.StringVar()
        self.species_var.set("Select a species")
        self.species_dropdown = ttk.OptionMenu(dropdown_frame, self.species_var, "Select a category first")
        self.species_dropdown.pack(side="left", padx=10) 

        scrollable_frame = self.create_scrollable_frame(self.library_tab)

        # Frame for species information and image (side by side)
        species_frame = tk.Frame(scrollable_frame, bg="#28666e")
        species_frame.pack(pady=0, fill=tk.X)

        # Info label for species description
        self.info_label = tk.Label(species_frame, text="", wraplength=700, justify="left", bg="#7c9885")
        self.info_label.pack(side="right", padx=40)

        # Image label for species image (to the right)
        self.image_label = tk.Label(species_frame, bg="black")
        self.image_label.pack(side="top", padx=20)
        

    def update_species_dropdown(self, selected_category):
        # Update species dropdown based on selected category
        species_list = self.categories.get(selected_category, [])
        menu = self.species_dropdown["menu"]
        menu.delete(0, "end")  # Clear current menu

        for species in species_list:
            menu.add_command(label=species, command=lambda s=species: self.display_species_info(s))

        # Reset species selection
        self.species_var.set("Select a species")

    def display_species_info(self, species):
        # Load the species image dynamically
        try:
            image_path = f"species_images/{species.lower()}.jpg" 
            species_image = Image.open(image_path)
            species_image = species_image.resize((250, 250))  #Resize image to fit the layout
            species_photo = ImageTk.PhotoImage(species_image)
            self.image_label.config(image=species_photo)
            self.image_label.image = species_photo  # Keep a reference to the image
        except Exception as e:
            print(f"Error loading image: {e}")
            self.image_label.config(image='')  # Clear image if not found

        # Species information
        species_info = {
            
        #=================MAMMALS=====================
            #Dolphin
            "Dolphin": 
            "Dolphins have smooth skin, flippers, and a dorsal fin. They have a long, slender snout with about 100 teeth, and a streamlined body.\n" 
            "The single blowhole on top of their head has a flap that opens to reveal a pair of nostrils, which dolphins use for breathing when they surface."
            "\n\n\nBehavior of Dolphins\n\n"
            "\nA. Social\n"
            "Dolphins are social animals that form pods and engage in a variety of social interactions, such as playing, breeding, and gentle body contact. They also help each other when a member is injured." 
            "\n\nB. Hunting\n"
            "Dolphins use a variety of foraging behaviors, including sponging, which involves using marine sponges to protect their rostrums while foraging."
            "They also use a behavior called shelling, where they chase a fish into an empty conch shell."
            "\n\nC. Communication\n"
            "Dolphins communicate using a variety of methods, including vocalizations, non-vocal acoustic cues, visual cues, and tactile cues."
            "\n\nD. Aerial\n"
            "Dolphins perform a variety of aerial behaviors, including nose-outs, tail slaps, back slaps, side slaps, head slaps, arcuate leaps, tail-over-head leaps, and spins." 
            "\n\nE. Learning\n"
            "Dolphins are known for their ability to learn and pass on behaviors, a phenomenon known as cultural transmission."
            "\n\nF. Interaction with humans\n"
            "Dolphins are curious and can develop affection for their caretakers. They can be easily disturbed by the presence of people and watercraft, especially when approached too closely, quickly, or noisily.\n\n"
            
            "\nDiet and Role in ecosystem\n\n"
            "Dolphins play a vital role in the ocean ecosystem by maintaining the balance of the food chain and regulating prey populations:\n"
            "\nA. Diet\n"
            "Dolphins are carnivorous apex predators that eat a variety of prey, including fish, squid, crustaceans, cuttlefish, and sometimes seals."
            "The type of prey a dolphin eats depends on its species and habitat. For example, orcas are larger dolphins that also eat marine mammals and birds."
            "\n\nB. Hunting techniques\n"
            "Dolphins use echolocation to locate prey by emitting sound waves and listening for echoes. They also use herding, where they work together to surround fish."
            "\n\nC. Food chain balance\n"
            "Dolphins keep the food chain in balance by preying on certain species and preventing them from overpopulating. They also eat sick or ill fish, which can help reduce infectious diseases among fish populations."
            "\n\nD. Ecological indicators\n"
            "Dolphins can help researchers identify imbalances in the ecosystem.\n\n"
            
            "\nHabitat\n\n"
            "Dolphins live in all of the world’s seas and oceans; many inhabit coastal areas or areas with shallower water. While most dolphins prefer warmer tropical or"
            "temperate waters one species, the orca (sometimes called killer whale) lives in both the Arctic Ocean and the Antarctic Southern Ocean."
            "Five dolphin species prefer fresh to salt water; these species inhabit rivers in South America and South Asia."
            "  \n\n\n"
            "  ",

            #Whale
            "Whale":
            "Whales are distributed throughout the world’s oceans and seas, from the Equator to the polar ice, except for the landlocked Caspian and Aral seas." 
            "They are mammals, and they share the defining traits of that group: they breathe air, are warm-blooded, give live birth, suckle their young on milk, and have hair." 
            "All are entirely aquatic, with specialized adaptations such as flippers and tail flukes for living in water. Whales must surface regularly to breathe,"
            "evacuating their lungs more completely than most mammals in an almost explosive breath known as a blow. Blows are visible because water vapour in the whale’s hot breath condenses when the blow is released."
            
            "\n\n\nBehavior of Whales\n\n"
            "Whales have many behaviors, including:"
            "\n\nA. Blowing\n"
            "When whales exhale, they force air out of their blowhole, creating a cloud of mist. This is the most common behavior to see from a whale. The shape of the mist can help identify the type of whale."
            "\n\nB. Tail Slapping\n"
            "Whales hang vertically in the water and beat the surface with their tail, creating loud cracks and splashes. This behavior is thought to be a way to communicate, defend themselves, or hunt."
            "\n\nC. Flipper Slapping\n"
            "Whales slap their pectoral flippers on the surface of the water, creating loud sounds underwater."
            "\n\nD. Breaching\n"
            "Whales breach the surface of the water. Researchers believe that breaching is a way for whales to communicate with each other."
            "\n\nE. Feeding\n"
            "Whales feed in different ways, such as lunging, where they take big gulps of water containing their prey, or skimming, where they swim with their mouths open and strain out their prey"
            "\n\nF. Social Behaviors\n"
            "Whales are social creatures that form strong bonds with other members of their pod. They rely on each other for survival. Some species give their calves names and greet each other when they meet."
            
            "\n\n\nDiet and Role in ecosystem\n\n"

            "A. Diet\n"
            "Whales have a variety of diets, depending on the species, their habitat, migration patterns, and season:"
            "\n\n    1. Baleen whales:\n "
            "These filter feeders, like blue and gray whales, eat small organisms like krill, plankton, and small fish. They swallow large gulps of water and strain it through their baleen plates."
            "\n\n    2. Toothed Whales:\n"
            "These whales, like orcas, have a broader diet and eat larger prey like fish, squid, and sometimes other marine mammals. They use echolocation to hunt their food. "
            "\n\nB. Nutrient distribution\n"
            "Whales contribute to nutrient distribution in the ocean through their feces, which are rich in nutrients that support phytoplankton growth."
            "\n\nC. Indicator of ocean health\n"
            "The presence of certain whale species can indicate the abundance of specific prey, providing valuable insights into the health of the marine ecosystem."
            
            "\n\n\nHabitat\n\n"
            "Whales live in every ocean on the planet. They can be found in temperate oceans and tropical waters around the equator, "
            "as well as in the freezing Arctic and Antarctic oceans. Some whale species can be found in seas, including the North Sea and the Mediterranean."
            "\n\n\n",

            #Seals
            "Seals":
            "Seals, also known as “earless” seals or simply “seals,” belong to a group of pinnipeds that have ear holes but lack an external ear flap."
            "Seals typically have a smaller body size compared to sea lions. But some, such as the Northern elephant seal and hooded seal, can be larger.\n\n"
            "On land, seals use their bellies to move around in a caterpillar-like motion. They have small front flippers that are thinly webbed with a claw on each small toe."
            "In the water, seals swim easily, moving their rear flippers back and forth, similar to how a fish uses its caudal fin (tail) to propel itself through the water."

            "\n\nBehavior of Seals"
            "\n\nSeals exhibit a variety of behaviors, including:"
            "\n\nA. Social interactions\n"
            "Seals can be timid, shy, and quiet, or boisterous, friendly, and playful. They can form closer bonds with other seals depending on their personality."
            "\n\nB. Hunting\n"
            "Seals dive to find food, such as sand eels and dargonets. They can sleep underwater and come up for air once every 30 minutes."
            "\n\nC. Communication\n"
            "Harbor seals use rhythmic percussive signaling to interact and display."
            "\n\nD. Learning\n"
            "Seals can perform many of the same sophisticated learning tasks as dolphins and apes."
            "\n\nE. Human Interaction\n"
            "Seals are naturally cautious of humans and are more likely to stay out of sight. However, some seals are tolerant of humans and may even snuggle up next to them. Males may occasionally view humans as rivals and charge."

            "\n\n\nDiet and Role in Ecosystem\n\n"
            "Seals are essential members of their ecosystems, both as predators of fish, squid, shellfish, seabirds, and other marine life and as prey for hunters like polar bears, orcas, and sharks."
            "Seals also provide important ecosystem services by increasing primary productivity in feeding areas,\n"
            "recycling both macro and micronutrients through returning massive amounts of nutrients through excrement, feeding plankton and other consumers up the food chain to humans."

            "\n\n\nHabitat\n\n"
            "Seals are found along most coasts and cold waters, but a majority of them live in the Arctic and Antarctic waters.\n"
            "When not at sea, common seals are found around sheltered shores and estuaries, where they haul out on sandbanks and beaches."
            "When out of the water, they sometimes hold their body in a curved banana position, with their head and tail both in the air at the same time."
            "\n\n\n",

            #Sea Lions
            "Sea Lions":
            "Sea lions are characterized by external ear flaps, long foreflippers, the ability to walk on all fours, short and thick hair, and a big chest and belly."
            "On land, sea lions use their large, elongated front flippers and rear flippers rotated underneath their bodies to “walk.” In the water, they propel themselves by paddling their front flippers and use their rear flippers to help steer, like a boat’s rudder."
            "\n\n\nBehavior of Sea Lions\n\n"
            "Sea lions exhibit a variety of behaviors, including:"
            "\n\nA. Social\n"
            "Sea lions are very social and engage in a variety of activities together, such as riding the surf, chasing each other, and pushing off rocks."
            "\n\nB. Territorial\n"
            "Sea lions engage in territorial battles."
            "\n\nC. Roaring\n"
            "Sea lions roar to help fend off predators."
            "\n\nD. Mating\n"
            "Females initiate courtship by displaying submissive postures to males. Copulation can take place on land or in water."
            "\n\nE. Responding to stimuli"
            "When they hear a loud noise or see rapid movement, some sea lions will head towards the water."
            "\n\nF. Swimming\n"
            "Sea lions can swim up to 35 miles per hour. They use their front flippers for swimming and their hind flippers for steering."
            "\n\nG. Hunting\n"
            "Sea lions are known to eat large quantities of food at a time, sometimes consuming 5–8% of their body weight in a single feeding."
            "\n\nH. Senses\n"
            "Sea lions have excellent vision, hearing, and smell. Their whiskers are sensitive to movement and can help them detect other animals."
            
            "\n\n\nDiet and Role in Ecosystem\n\n"
            "A. Diet\n\n"
            "Sea lions are primarily piscivorous, eating a variety of fish, squid, octopus, crabs, and clams. The type of fish they eat depends on the species and location, but can include herring, rockfish, anchovies, salmon, and hake."
            "Sea lions can consume large quantities of food at a time, about 5 to 8% of their body weight."
            "\n\nB. Ecosystem indicators\n\n"
            "Changes in a sea lion's diet over time can indicate changing ocean conditions that affect the availability of their prey."
            "These shifts in diet can impact the sea lion's body condition, reproductive success, and population survival."
            "\n\nC. Role in the ecosystem\n\n"
            "Sea lions are predators that remove fish and energy from the system. However, some models suggest that fish are more important predators of other fish than sea lions."
            
            "\n\n\nHabitat\n\n"
            "Sea lions can be found along the coastlines and islands of the Pacific Ocean. They are adapted for life on land and at sea. They have strong front flippers that support them on land and also help regulate their body temperature."
            "Their sleek body helps them to make deep dives to catch prey, up to 600 feet." 
            "They are strong swimmers that can reach speeds of 18 miles per hour. They are able to stay underwater for 10 to 20 minutes at a time with the help of their nostrils, but they must come up to breathe."
            "\n\n\n",

            #Otters
            "Sea Otters":
            "Sea otters are part of the weasel family. They have webbed feet, water-repellent fur to keep them dry and warm, and nostrils and ears that close in the water."
            "Sea otters are the only otters to give birth in the water. Mothers cuddle their young while floating on their backs and hold infants on their chests to nurse them. They quickly teach them to swim and hunt for themselves."
            "Sea otters have the thickest fur of any animal, with up to one million hairs per square inch. This fur helps them maintain their body temperature in cold water, keeps them dry when submerged, and provides buoyancy."
            "\n\n\nBehavior of Sea Otters\n\n"
            "Sea otters are known for being playful, curious, and social animals:"
            "\n\nA. Playful\n"
            "Sea otters are known for wrestling with each other, especially as pups. This wrestling is a form of play and helps young otters learn social cues."
            "\n\nB. Social\n"
            "Sea otters are social animals, and females and their pups are often seen together in groups."
            "\n\nC. Tool User\n"
            "Sea otters are one of the few animals that use tools, such as rocks, to break open shellfish like clams and abalone."
            "\n\nD. Communication\n"
            "Sea otters communicate through body contact, head-jerking, vocalizations, and nosing each other. Adults make soft coos and grunts to express contentment."
            "\n\n\n---Diet---\n\n"
            "Sea otters eat a variety of invertebrates, including crabs, snails, urchins, clams, abalone, and mussels."
            "They also eat fish in the north. Sea otters are known to specialize in certain types of prey, even when foraging in the same area with other otters of the same age and sex"
            "\n\n\n---Role in Ecosystem---\n\n"
            "Sea otters are a keystone species, meaning they have a disproportionate impact on their environment. They help maintain the balance of nearshore ecosystems by keeping the populations of other animals in check:"
            "\n\nA. Kelp forest\n"
            "Sea otters eat sea urchins, which are voracious consumers of kelp."
            "Without sea otters, urchin populations can explode and destroy kelp forests, which provide food and shelter for other marine animals."
            "Healthy kelp forests also sequester carbon, which helps reduce ocean warming and acidification."
            
            "\n\nB. Estuaries\n"
            "Sea otters eat crabs, which allows sea slug populations to thrive. Sea slugs eat algae that would otherwise smother the eelgrass that fish need for food and shelter."
            "\n\nC. Trophic cascade\n"
            "Sea otters are an example of a trophic cascade, which is the system of organisms eating each other in an ecosystem."
            "In this system, sea otters eat crabs, which eat seagrass, which eat algae."
            
            "\n\n\nHabitat\n\n"
            "The Sea Otter lives in areas where it can dive for food in the Pacific Ocean, most often within one to two kilometres from shore where the water is no more than 40 metres deep."
            "Shallow rocky reefs and kelp forests are ideal for prey abundance, but also for resting (or rafting) in their calmer waters. In calm weather, otters tend to be active in exposed areas, but they will head for bays and inlets during storms, especially in the winter."
            "\n\nSea Otters are found in a wide range of water temperatures, but they are restricted by the Arctic sea ice in the north. They are not migratory."
            "\n\n\n",

            #Manatees
            "Manatees":
            "Manatees are large, gray aquatic mammals. They may appear more green or brown due to organisms like algae that grow on the skin.\n"
            "Manatees have split lips and hairy, creased faces. They are fish-shaped, and have hairless skin, with paddle-like forelimbs and horizontal tail which is broadly rounded and shovel-like, not divided into two lobes as in the dugong."
            "They have mobile flippers which can be used as hands. The colour is dark grey to blackish. Their upper lips are divided and mobile. Manatees use their top and bottom lips together in order to grasp and tear at their food."
            "\n\n\nBehavior of Manatees\n\n"
            "Manatees are semi-social, nonaggressive, and nonterritorial mammals with a variety of behaviors:"
            "\n\nA. Feeding\n"
            "Manatees spend six to eight hours a day eating seagrasses and other aquatic plants. They may also occasionally eat small fish and invertebrates"
            "\n\nB. Resting\n"
            "Manatees spend two to twelve hours a day resting. They sleep submerged for about half of the day, surfacing for air every 20 minutes or less."
            "\n\nC. Traveling\n"
            "Manatees spend the rest of their day traveling. They are strong swimmers that can reach speeds of up to 15 miles per hour in short bursts"
            "\n\nD. Social\n"
            "Manatees are generally solitary, except for mothers with their young and males following a receptive female. Socializing behaviors include touching noses, chewing along the body, and close following."
            "\n\nE. Mating\n"
            "A small herd of males will follow a female in estrus, and several may mate with her in succession."
            "\n\nF. Boldness-shyness\n"
            "Manatees can exhibit boldness-shyness traits, with bolder individuals approaching stimuli more and for longer than shier individuals"
            "\n\n\nDiet\n\n"
            "Manatees eat a variety of aquatic vegetation based on where they are located.\n"
            "They have been documented eating over 60 different varieties of vegetation including turtle grass, manatee grass, shoal grass, mangrove leaves, water hyacinth, hydrilla, and eelgrass."
            "\n\nManatees have very poor vision and have trouble seeing where their favorite food sources out. Luckily, manatees have over 2000 sensitive whiskers on their faces called vibrissae to feel for food in the water."
            "With this special adaptation, they can discover seagrass as they float through different freshwater and saltwater habitats."
            "\n\nIn ideal conditions, Manatees spend up to 8 hours a day grazing on aquatic plants. But when the weather is cold and the water temperatures drop, manatees will move to warm water sources where there may not be enough food. During these times, manatees conserve their energy and can survive weeks without eating."
            
            "\n\n\nRole in Ecosytem\n\n"
            "Manatees are keystone species, meaning that many other animals depend on them for survival. If manatees were to become extinct, many species of fish, seahorses, starfish, clams, crabs, sea turtles, and coastline birds could also be at risk"
            "Manatees eat a LOT of sea grass. By doing so, they keep the grass short, which helps maintain the health of the sea grass beds. While manatees don't have any true natural predators, they have still become endangered."
            
            "\n\n\nHabitat\n\n"
            "Manatees can be found in shallow, slow-moving rivers, estuaries, saltwater bays, canals, and coastal areas—particularly where seagrass beds or freshwater vegetation flourish.\n"
            "Manatees are a migratory species. Within the United States, they are concentrated in Florida in the winter."
            "\n\n\n",

        #=================PLANTS=====================

            #Phytoplankton
            "Phytoplankton":
            "Phytoplankton, also known as microalgae, are similar to terrestrial plants in that they contain chlorophyll and require sunlight in order to live and grow."
            "Most phytoplankton are buoyant and float in the upper part of the ocean, where sunlight penetrates the water.\n\n"
            "Like land plants, phytoplankton have chlorophyll to capture sunlight, and they use photosynthesis to turn it into chemical energy. They consume carbon dioxide, and release oxygen."
            "All phytoplankton photosynthesize, but some get additional energy by consuming other organisms.\n\n"
            "Phytoplankton growth depends on the availability of carbon dioxide, sunlight, and nutrients. Phytoplankton, like land plants, require nutrients such as nitrate, phosphate, silicate, and calcium at various levels depending on the species."
            "Some phytoplankton can fix nitrogen and can grow in areas where nitrate concentrations are low. They also require trace amounts of iron which limits phytoplankton growth in large areas of the ocean because iron concentrations are very low."
            "Other factors influence phytoplankton growth rates, including water temperature and salinity, water depth, wind, and what kinds of predators are grazing on them.\n\n"
            "Phytoplankton can grow explosively over a few days or weeks."
            "When conditions are right, phytoplankton populations can grow explosively, a phenomenon known as a bloom. Blooms in the ocean may cover hundreds of square kilometers and are easily visible in satellite images."
            " A bloom may last several weeks, but the life span of any individual phytoplankton is rarely more than a few days"
            
            "\n\n\nImportance of Phytoplankton\n\n"
            "Phytoplankton are the foundation of the aquatic food web, the primary producers, feeding everything from microscopic, animal-like zooplankton to multi-ton whales. Small fish and invertebrates also graze on the plant-like organisms,"
            "and then those smaller animals are eaten by bigger ones.\n\n"
            "Phytoplankton can also be the harbingers of death or disease. Certain species of phytoplankton produce powerful biotoxins, making them responsible for so-called “red tides,” or harmful algal blooms."
            "These toxic blooms can kill marine life and people who eat contaminated seafood."
            
            "\n\n\nSpecies composition\n\n"
            "Hundreds of thousands of species of phytoplankton live in Earth's oceans, each adapted to particular water conditions. Changes in water clarity, nutrient content, and salinity change the species that live in a given place.\n\n"
            "Because larger plankton require more nutrients, they have a greater need for the vertical mixing of the water column that restocks depleted nutrients. As the ocean has warmed since the 1950s,"
            "it has become increasingly stratified, which cuts off nutrient recycling.\n\n"
            "Continued warming due to the build up of carbon dioxide is predicted to reduce the amounts of larger phytoplankton such as diatoms), compared to smaller types, like cyanobacteria. "
            "Shifts in the relative abundance of larger versus smaller species of phytoplankton have been observed already in places around the world, but whether it will change overall productivity remains uncertain."
            "\n\n\n",

            #Seagrasses
            "Seagrasses":
            "Seagrasses are found in shallow salty and brackish waters in many parts of the world, from the tropics to the Arctic Circle. Seagrasses are so-named because most species have long green, grass-like leaves."
            "They are often confused with seaweeds, but are actually more closely related to the flowering plants that you see on land. Seagrasses have roots, stems and leaves, and produce flowers and seeds."
            "They evolved around 100 million years ago, and today there are approximately 72 different seagrass species that belong to four major groups.\n\n"
            "Seagrasses can form dense underwater meadows, some of which are large enough to be seen from space. Although they often receive little attention, they are one of the most productive ecosystems in the world."
            "Seagrasses provide shelter and food to an incredibly diverse community of animals, from tiny invertebrates to large fish, crabs, turtles, marine mammals and birds. Seagrasses provide many important services to people as well,"
            "but many seagrasses meadows have been lost because of human activities.\n\n\n"
            "Where are Seagrasses found?\n\n"
            "Seagrasses grow in salty and brackish (semi-salty) waters around the world, typically along gently sloping, protected coastlines. Because they depend on light for photosynthesis, they are most commonly found in shallow depths where light levels are high. "
            "Many seagrass species live in depths of 3 to 9 feet (1 to 3 meters), but the deepest growing seagrass (Halophila decipiens) has been found at depths of 190 feet (58 meters)."
            "While most coastal regions are dominated by one or a few seagrass species, regions in the tropical waters of the Indian and western Pacific oceans have the highest seagrass diversity with as many as 14 species growing together."
            "Antarctica is the only continent without seagrasses."
            "\n\n\nEcosystem Benefits\n\n"
            "Seagrasses are often called foundation plant species or ecosystem engineers because they modify their environments to create unique habitats. These modifications not only make coastal habitats more suitable for the seagrasses themselves, "
            "but also have important effects on other animals and provide ecological functions and a variety of services for humans.\n\n"
            "Seagrasses have been used by humans for over 10,000 years. They've been used to fertilize fields, insulate houses, weave furniture, thatch roofs, make bandages, and fill mattresses and even car seats. But it's what they do in their native habitat that has the biggest benefits for humans and the ocean. "
            "Seagrasses support commercial fisheries and biodiversity, clean the surrounding water and help take carbon dioxide out of the atmosphere. Because of these benefits, seagrasses are believed to be the third most valuable ecosystem "
            "in the world (only preceded by estuaries and wetlands). One hectare of seagrass (about two football fields) is estimated to be worth over $19,000 per year, making them one of the most valuable ecosystems on the planet."
            "\n\n\n",
            
            #Algae
            "Algae":
            "The term algae is from the Latin alga, meaning “seaweed”. The descriptive word algal pertains to, characterizes, or relates to alga(e). "
            "Algae, members of a group of predominantly aquatic photosynthetic organisms of the kingdom Protista. Algae have many types of life cycles, "
            "and they range in size from microscopic Micromonas species to giant kelps that reach 60 metres (200 feet) in length. Their photosynthetic pigments are more varied than those of plants, "
            "and their cells have features not found among plants and animals.\n\n"
            "In addition to their ecological roles as oxygen producers and as the food base for almost all aquatic life, "
            "algae are economically important as a source of crude oil and as sources of food and a number of pharmaceutical and industrial products for humans."
            "\n\n\nEcological and commercial importance\n\n"
            "Algae form organic food molecules from carbon dioxide and water through the process of photosynthesis, in which they capture energy from sunlight."
            "Similar to land plants, algae are at the base of the food chain, and, given that plants are virtually absent from the oceans, the existence of nearly "
            "all marine life—including whales, seals, fishes, turtles, shrimps, lobsters, clams, octopuses, sea stars, and worms—ultimately depends upon algae."
            "\nIn addition to making organic molecules, algae produce oxygen as a by-product of photosynthesis. Algae produce an estimated 30 to 50 percent of the net global oxygen available to humans and other terrestrial animals for respiration."
            "\n\n\nToxicity\n\n"
            "Some algae can be harmful to humans. A few species produce toxins that may be concentrated in shellfish and finfish, which are thereby rendered unsafe or poisonous for human consumption.\n"
            "Algae can cause human diseases by directly attacking human tissues, although the frequency is rare. Protothecosis, caused by the chloroplast-lacking green alga, Prototheca, can result in waterlogged skin lesions, in which the pathogen grows."
            "\n\n\n",

            #Kelp
            "Kelp":
            "Kelp is a large brown seaweed (also called marine algae) that grows mainly in underwater kelp forests on the Pacific Coast, both near North America and South America."
            "Physically the kelps appear to be plants. The main body consists of a holdfast resembling roots that attaches to a substratum. While they remain attached, the body of the kelp remains floating and appears to be dancing on the tunes of ocean currents. "
            "The short branches like stipes resemble a stem whereas its blades appear to be the leaves. Kelp blades reach to the available light near the surface of the ocean through floats or pneumocystis which are gas-filled compartments otherwise known as gas bladders. "
            "They grow in dense groupings much like a forest on land, and are found predominantly along the Pacific coast from Alaska to parts of Baja California. You can see kelp forests in many of our national marine sanctuaries."
            "\n\n\nImportance of Kelp Forest\n\n"
            "Kelp forests are often regarded as “underwater rainforests”. Formed by the dense growth of several kelp species, they produce a three-dimensional habitat and a highly productive system. Usually found in water temperatures below 20 °C, kelps are large brown algae that attach to the seafloor. "
            "Not only can kelps grow amazingly fast in the right conditions – up to 30 cm per day – they can also reach 45 m long for the giant kelp. As well as providing plenty of surfaces and nooks and crannies for other species to settle on or in and live, "
            "they shelter coastlines from storms and help sequester or absorb carbon from the atmosphere, making them incredibly important societal resources.\n\n"
            "Unfortunately, kelp forests today face a variety of threats, such as commercial kelp harvesting, pollution, and climate change, are negatively impacts kelp reproduction and survival.\n"
            "Overgrazing by fish and sea urchins is a particularly large problem for kelp forests. Predators such as sea otters and sea stars typically keep populations of urchins and grazing fishes in check; this keeps the numbers of urchins and fish in balance so they don't mow down entire kelp forests. "
            "However, recent declines in otters and sea stars on the West Coast have led to an explosion in the number of urchins, which is bad news for kelp forests as they face increased grazing."
            "\n\n\n",

            #Sargassum
            "Sargassum":
            "Sargassum is a genus of brown macroalgae in the order Fucales of the Phaeophyceae class. Numerous species are distributed throughout the temperate and tropical oceans of the world, where they generally inhabit shallow water and coral reefs, and the genus is widely known for its planktonic species"
            "\n\n\nEssential Fish Habitat\n\n"
            "Free-floating Sargassum in the ocean provides habitat, food resources, protection, and breeding grounds for hundreds of marine species. This includes commercially important fisheries species such as gray triggerfish, amberjack, and mahi mahi that feed on the smaller marine life present in Sargassum mats."
            "In the South Atlantic, Gulf of Mexico, and the Caribbean, NOAA designates areas of Sargassum as Essential Fish Habitat. Juvenile sea turtles and sea birds also use Sargassum for feeding and shelter. "
            "In the South Atlantic and portions of the Gulf of Mexico, Sargassum is designated as Critical Habitat for threatened loggerhead sea turtles under the Endangered Species Act."
            "\n\n\nSargassum Inundation Events on Shore\n\n"
            "When excessive amounts of Sargassum reach the shore, it is referred to as a" "Sargassum inundation event," "or SIE for short. "
            "Sargassum inundation events occur when rafts of this algae are carried to shore by winds and currents. These events are a type of harmful algal bloom that can adversely impact coastal ecosystems, tourism, and public health. Massive amounts of Sargassum can form brown tides nearshore, smothering fauna and flora — including coral reefs.\n\n"
            "Sargassum mats may also clog water intake pipes used in critical infrastructure (for example, in desalination plants that produce drinking water). Sargassum also contains high levels of arsenic and other heavy metals, organic contaminants, and marine debris."
            "Sargassum decomposing on the beach produces hydrogen sulfide, a gas that smells like rotten eggs, which can cause respiratory irritation. "
            "\n\n\nThe Many Sargassum Uses – Upcycling for Good\n\n"
            "Carbonwave has found that sargassum contains a number of beneficial components that can be extracted and used to create other products that various industries desperately need – but it must be done in a way that’s sustainable and keeps the good elements of sargassum intact throughout the extraction process."
            "\n\n\n",

        #===================Ocean Fishes======================
            
            #Shark
            "Shark":
            "Sharks are fishes. Like other fishes, sharks are cold-blooded, have fins, live in the water, and breathe with gills. A shark's skeleton is made of cartilage. "
            "A shark's fusiform (rounded and tapering at both ends) body shape reduces drag and requires minimum energy to swim. Sharks eat far less than most people imagine.\n\n"
            "The skin typically is dull gray and tough and has toothlike scales. Most sharks have a muscular, asymmetrical, upturned tail; pointed fins; a pointed snout; and sharp triangular teeth. "
            "Sharks have no swim bladder and must swim perpetually to keep from sinking. Most species bear living young."
            "\n\n\nBahavior of a shark\n\n"
            "A sharks behaviour is completely linked to their amazing array of senses. These senses influence every part of their lives."
            "Low frequency sounds can travel great distances under the water and the sharks complex hearing system allows them to be the first to detect an interesting target.\n\n"
            "Depending on species, sharks can be either solitary, gliding through the water in search of food, or gregarious in the form of schools containing over 100 individuals. "
            "The Scalloped Hammerheads are a prime example of one species of shark that congregate in large numbers. However, even solitary sharks occasionally meet for mating or on hunting grounds which may lead them to cover thousands of miles a year."
            "\n\n\nAre sharks intelligent?\n\n"
            "Despite the common myth that sharks are instinct-driven eating machines, recent studies have indicated that many species possess powerful problem-solving skills, social complexity and curiosity."
            "The brain-mass-to-body-mass ratios of sharks are similar to those of mammals and other higher vertebrate species."
            "\n\nDespite the common myth that sharks are instinct-driven eating machines, recent studies have indicated that many species possess powerful problem-solving skills, social complexity and curiosity."
            "The brain-mass-to-body-mass ratios of sharks are similar to those of mammals and other higher vertebrate species."
            "\n\nGroups of sharks, roughly the same age and gender, tend to return to the same area each year."
            "Sharks have been observed returning to a particular place and patrol the same bays every year at the same time. Each year, they bask and communicate with each other with body movements and are present at each others kills. A particular species renown for this behaviour is the Grey Reef Shark."
            "\n\n\nDo Sharks Sleep?\n\n"
            "Sharks need to keep moving in order to breathe, however some shark species have been observed resting on the sea bed actively pumping water over their gills. Sharks tend to have active and inactive periods rather than sleep."
            "\n\n\nImportance of Sharks\n\n"
            "As apex predators, sharks play an important role in the ecosystem by maintaining the species below them in the food chain and serving as an indicator for ocean health. They help remove the weak and the sick as well as keeping the balance with competitors helping to ensure species diversity."
            "\n\n\nDiet\n\n"
            "Sharks are carnivores, and they primarily hunt and eat fish, sea mammals like dolphins and seals, and other sharks. Some species prefer or include turtles and seagulls, crustaceans and mollusks, and plankton and krill in their diets."
            "\n\n\nHabitat of Sharks\n\n"
            "Sharks are found from shallow to deep sea environments, in coastal, marine and oceanic environments the world over. Some species inhabit shallow, coastal regions, while others live in deep waters, on the ocean floor and in the open ocean. "
            "A few species, such as the bull shark, move easily through salt, fresh and brackish waters."
            "\n\n\n",

            #Seahorse
            "Seahorse":
            "The oddly shaped and upright-swimming seahorse seems an unlikely fish. Yet more than 45 species live in coastal waters around the globe. Scientists have learned their basic biology, but much remains unknown about these charismatic animals."
            "\n\nIts head may resemble a horse’s, but each seahorse has a look all its own. Most are spotted, speckled, or striped, and some are decked out in skin frills, spikes, and crowns. Colors vary and can change with the twitch of a muscle to offer camouflage or to signal a foe or potential mate."
            "\n\nSeahorses have flesh-covered bony plates instead of scales, eyes that work independently of each other, and prehensile tails—used to grip holdfasts on the seafloor to avoid drifting and, during courtship, to link to each other."
            "\n\nThe tiniest species is no bigger than a lima bean; the largest can reach more than a foot from head to tail tip."
            "\n\n\nBehaviour of Seahorse\n\n"
            "Seahorses are weak swimmers that use their prehensile tails to anchor themselves to plants and corals within their small home ranges. They are ambush predators, relying on their long snouts to suck in tiny prey like brine shrimp and plankton."
            "Known for their unique courtship rituals, seahorses engage in nose-to-nose embraces, tail twisting, and graceful dances. Remarkably, it is the male seahorse that carries the eggs in a brood pouch and gives birth to fully developed baby seahorses, called fry."
            "They communicate through vision, touch, sound, vibrations, and chemicals, with mating pairs producing a clicking sound when touching heads. Additionally, they use camouflage to blend into their environments, with some, like the pygmy seahorse, resembling coral, while others, like the thorny seahorse, can change their colors."
            "\n\n\nDiet\n\n"
            "Seahorses are ambush predators, remaining motionless and camouflaged in their surroundings as they wait for tiny prey like krill, copepods, fish larvae, and other small edibles to drift close. When an unsuspecting meal comes within range, they strike with astonishing speed, using their elongated, tube-like snouts to create a powerful suction that draws the prey directly into their mouths."
            "Without teeth to chew or a stomach to store food, seahorses rely on near-continuous feeding to sustain their energy needs. Their specialized snouts function like precision vacuum cleaners, allowing them to consume large quantities of plankton and other tiny organisms throughout the day. This constant feeding strategy is vital, as their lack of a stomach means food is processed quickly and does not linger in their digestive system."
            "\n\n\nHabitat\n\n"
            "Preferring calm, shallow waters, seahorses thrive in seagrass beds, mangroves, estuaries, and coral reefs in temperate and tropical waters around the world. Relatively inept swimmers, the fish get around with frantic beats (up to 70 times per second) of a dorsal (back) fin and rely on tiny pectoral fins for stability and steering. Easily exhausted, many are swept away in heavy currents or killed in storm-roiled seas."
            "\n\n\n",

            #Bluefin Tuna
            "Bluefin Tuna":
            "Bluefin are the largest tunas and can live up to 40 years. They migrate across all oceans and can dive deeper than 3,000 feet. Bluefin tuna are made for speed: built like torpedoes, have retractable fins and their eyes are set flush to their body."
            "They are tremendous predators from the moment they hatch, seeking out schools of fish like herring, mackerel, and even eels."
            "They hunt by sight and have the sharpest vision of any bony fish. There are three species of bluefin: Atlantic (the largest and most endangered), Pacific, and Southern."
            "Most catches of the Atlantic bluefin tuna are taken from the Mediterranean Sea, which is the most important bluefin tuna fishery in the world."
            "\n\n\nBehaviour of Bluefin Tuna\n\n"
            "Bluefin tuna are highly social and migratory fish known to form massive schools, especially in their youth, using sight and possibly other senses to stay coordinated."
            "They travel vast distances, inhabiting temperate, tropical, and cooler coastal regions, and adapt their movements based on environmental conditions."
            "As intelligent hunters, they strategically consider water temperature, chlorophyll levels, and ocean currents to locate prey and remain in waters that optimize digestion."
            "Interestingly, they are also observed basking in the sun during the afternoon. While they lack fixed home ranges, they belong to populations that migrate between seasonal home ranges."
            "Pacific bluefin tuna display exceptional maneuverability, performing both slower global ratchet turns and much faster local ratchet turns. Additionally, Atlantic bluefin tuna exhibit unique post-release behavior,"
            "diving rapidly before leveling off and swimming horizontally after being caught and released."
            "\n\n\nDiet\n\n"
            "Bluefin tuna are opportunistic and highly efficient predators with a carnivorous diet that includes a wide range of marine organisms."
            "They primarily hunt small fish such as mackerel, herring, sardines, and anchovies, which provide them with the necessary energy and nutrients."
            "Squid is another major component of their diet, offering high protein and fat content essential for their fast-swimming lifestyle. Additionally, bluefin tuna may feed on crustaceans like shrimp or crabs, depending on availability in their habitat."
            "In their juvenile stages, bluefin tuna may also consume planktonic organisms before transitioning to larger prey as they grow. Their feeding habits are influenced by environmental factors like water temperature, chlorophyll levels, and the abundance of prey species,"
            "and they can adjust their hunting techniques accordingly. With their powerful swimming abilities, excellent vision, and highly efficient metabolism, bluefin tuna are capable of capturing and consuming large quantities of food to sustain their energy needs, supporting their migratory and hunting behaviors."
            "\n\n\nHabitat\n\n"
            "Bluefin tuna inhabit a variety of oceanic environments across the world, with different species preferring distinct regions."
            "Atlantic bluefin tuna are found in the North Atlantic Ocean and the Mediterranean Sea,"
            " where they move between temperate waters for feeding and warmer waters for spawning. Pacific bluefin tuna primarily reside in the northern Pacific Ocean,"
            " from the coasts of Japan to the U.S. West Coast, migrating long distances between tropical waters for breeding and cooler, nutrient-rich waters for feeding."
            "Southern bluefin tuna are located in the Southern Hemisphere, typically around Australia, New Zealand, and southern Africa, where they follow seasonal migratory patterns between feeding and breeding areas."
            " Bluefin tuna are primarily pelagic, spending most of their lives in the open ocean, and prefer deep, offshore waters. However, they are also found in coastal regions, especially when feeding or during migration."
            " Their migration routes and habitat preferences are strongly influenced by water temperatures, prey availability, and seasonal changes, as they seek optimal conditions for survival and reproduction."
            "\n\n\n",

            #Eel
            "Eel":
            "Eels are elongated, snake-like fish with smooth, slimy skin, sharp teeth, and powerful jaws, often exhibiting nocturnal, predatory behavior while hiding in crevices or burrows;"
            " they play an important role in marine ecosystems as solitary hunters, feeding on fish, crustaceans, and mollusks, and some species have complex migratory and reproductive patterns."
            "Eels display a range of fascinating behaviors that contribute to their survival in various marine environments. Most eel species are nocturnal, emerging from their hiding spots at night to hunt for food,"
            " while spending their daylight hours resting in crevices, coral reefs, or burrows to avoid predators and conserve energy. As solitary creatures, eels typically do not form groups, preferring to establish territories where they seek shelter and food."
            "\n\n\nBehaviour or Eels\n\n"
            " They are carnivorous predators, often ambushing small fish, crustaceans, and mollusks by waiting in hiding or slowly swimming toward their prey before striking swiftly with their sharp teeth and strong jaws. Some species, like moray eels, exhibit territorial behavior,"
            " defending their preferred resting spots from intruders. In terms of reproduction, eels such as the European eel have complex life cycles, migrating thousands of miles from their freshwater or coastal habitats to spawn in the open ocean, often in specific areas like the Sargasso Sea."
            " These migrations are critical for their reproduction, after which many species die, completing their life cycle. Overall, eels are skilled, stealthy hunters with unique social and migratory behaviors that help them thrive in the diverse marine habitats they occupy."
            "\n\n\nDiet\n\n"
            "Eels are primarily carnivorous and opportunistic predators, feeding on a variety of small marine organisms. Their diet mainly consists of fish such as small baitfish, juvenile fish, and occasionally larger fish if the opportunity arises."
            " They also consume crustaceans like shrimp, crabs, and lobsters, as well as mollusks such as squid and snails. Some eel species, especially moray eels, may also feed on smaller invertebrates like worms and sea urchins."
            " Eels are skilled hunters, often relying on stealth and ambush tactics to capture their prey, using their sharp, backward-facing teeth to grasp and hold onto their catch. They are known to forage at night, when they emerge from their hiding places in crevices or burrows to hunt."
            " Due to their lack of a stomach, eels must feed frequently, consuming large amounts of food to sustain their energy levels."
            "\n\n\nRole in Ecosystem\n\n"
            "Eels play an important role in aquatic ecosystems as both predators and prey. As predators, they help regulate populations of smaller fish, crustaceans, and invertebrates, maintaining balance in the food web. Their diet often includes fish larvae, invertebrates, and even smaller eels. Eels are also scavengers,"
            " feeding on detritus and decaying organic matter, which helps recycle nutrients back into the ecosystem. Additionally, eels serve as prey for a variety of larger predators, including fish, birds, and mammals. In estuarine and freshwater environments, eels contribute to the overall biodiversity"
            " and health of the ecosystem by participating in nutrient cycling and supporting food chains."
            "\n\n\nHabitat\n\n"
            "Eels are highly adaptable and can be found in a diverse range of habitats across both marine and freshwater environments. Species like moray eels typically inhabit tropical and subtropical coastal waters,"
            " favoring areas with abundant shelter such as coral reefs, rocky crevices, and underwater caves, where they can hide during the day and emerge at night to hunt."
            " On the other hand, conger eels are generally found in deeper offshore waters, such as continental shelves, underwater canyons, and seamounts, where they live in burrows or crevices along the ocean floor, often in colder regions compared to morays."
            "\n\nAnguillid eels, like the European eel and American eel, are anadromous, meaning they live in freshwater or estuarine habitats, such as rivers, lakes, and coastal waters, for most of their lives, but they migrate to the open ocean, particularly the Sargasso Sea, for spawning."
            "Throughout their life cycle, eels seek out habitats that provide protection from predators, such as hidden caves or burrows, and are often nocturnal, emerging primarily at night to hunt for food."
            " The variety of eel species and their adaptability to different environments—ranging from shallow coastal zones to the deep sea—demonstrates their ability to thrive in both fresh and saltwater ecosystems."
            "\n\n\n",

        #====================OTHERS========================

            "Octopus":
            "Octopuses are fascinating, highly intelligent marine creatures known for their unique physical and behavioral traits."
            " Their soft, boneless bodies allow them to contort and squeeze through tight spaces, making them highly adaptable to their environments."
            " They possess eight long, flexible arms that are lined with hundreds of suction cups, which not only help them grasp objects and capture prey but also allow them to sense their surroundings by taste and touch."
            " Their remarkable ability to change color and texture through specialized skin cells called chromatophores helps them blend into their surroundings for camouflage, aiding in both predation and defense."
            "\n\nWith excellent vision, octopuses have large eyes that can adjust to different light conditions, providing them with a sharp sense of sight to detect prey and predators."
            " They are also capable of using jet propulsion to move quickly through water, expelling water from a siphon to propel themselves in the opposite direction, often to escape threats."
            " As a defense mechanism, they can release a cloud of ink to disorient predators and make a quick getaway. Octopuses are known for their intelligence, demonstrating problem-solving abilities, tool use, and complex behaviors like opening jars and navigating mazes."
            " Despite their remarkable adaptability and skills, most octopuses have relatively short lifespans, typically living just 1 to 5 years."
            "\n\n\nBehaviour of Octopus\n\n"
            "Octopuses are highly intelligent and solitary creatures, primarily active at night as they hunt for prey, using their remarkable camouflage abilities to blend into their surroundings and ambush unsuspecting fish, crustaceans, and mollusks."
            " Their behavior is characterized by exceptional problem-solving skills, such as opening jars or using tools, and they can navigate complex environments with ease, often escaping from enclosures or tight spaces due to their boneless bodies."
            "\n\nWhile they generally prefer solitude, octopuses can communicate with each other through body language, changing the color and texture of their skin to display aggression or mating signals."
            " In terms of reproduction, males transfer sperm to females using a specialized arm, and after laying eggs, the females guard them until they hatch, often dying shortly after reproduction."
            " As a defense mechanism, octopuses can expel ink to disorient predators, allowing them to make a swift escape. Overall, octopus behavior is a blend of intelligence, adaptability, and defensive strategies, making them one of the most fascinating creatures in the ocean."
            "\n\n\nDiet\n\n"
            "Octopuses are carnivorous predators with a diet primarily consisting of small fish, crustaceans, mollusks, and other marine invertebrates. They hunt by using their excellent camouflage to ambush prey, often hiding in crevices or under rocks and then striking quickly with their arms."
            " They use their sharp beak to break open shells or tear apart soft-bodied animals. Some octopuses may also eat larger prey if the opportunity arises, including other cephalopods."
            " Their feeding habits vary depending on the species and their environment, but they generally rely on a diet rich in protein to sustain their energy needs."
            "\n\n\nRole in Ecosystem\n\n"
            "As skilled hunters, they help regulate populations of crustaceans, fish, and other small marine creatures, maintaining balance in the food web. Octopuses are solitary hunters, using their intelligence and camouflage abilities to catch prey,"
            " often ambushing them or using tools. As prey, they are an important food source for larger predators like sharks, seals, and larger fish. By preying on various organisms, octopuses also contribute to controlling populations of certain species,"
            " which helps sustain biodiversity. Their behavior, such as burrowing into the seafloor and using hiding spots, also creates opportunities for other marine creatures to find shelter. Overall, octopuses contribute to maintaining the stability and health of marine ecosystems."
            "\n\n\nHabitat\n\n"
            "Octopuses inhabit a wide range of marine environments, from shallow coastal waters to deep ocean floors. They are commonly found in coral reefs, rocky shorelines, and muddy or sandy seabeds, where they can hide in crevices, caves, or burrows."
            " Some species prefer tropical and temperate waters, while others are found in cold deep-sea environments. Octopuses are often solitary, and their choice of habitat typically provides plenty of shelter for protection from predators and a place to hunt for food."
            "\n\nThey may live in areas with abundant cover, such as under rocks, in abandoned shells, or in natural cavities, allowing them to stay hidden during the day and emerge at night to hunt. Some species, like the giant Pacific octopus, can be found at depths of over 200 meters,"
            " while others, like the common octopus, inhabit shallow waters down to about 100 meters deep."
            "\n\n\n",

            #Crabs
            "Crabs":
            "Crabs are crustaceans belonging to the order Decapoda, known for their distinctive hard exoskeleton, which provides protection, and their ten limbs—eight walking legs and two pincers, which are often asymmetrical."
            " These pincers are used for defense, capturing prey, and communication. Crabs have well-developed compound eyes mounted on stalks, allowing them to detect movement and threats from various directions. Unlike other crustaceans,"
            " crabs have a shortened abdomen, which is typically folded beneath their body, a feature that sets them apart from species like lobsters. "
            "\n\nThey have a tough exoskeleton made of chitin and calcium carbonate, which they periodically molt to grow. Crabs are highly adaptable, inhabiting a variety of environments,"
            " from marine ecosystems to freshwater habitats and even terrestrial regions. They are omnivores, feeding on a wide range of plant material, smaller animals, and detritus. Communication is often through body language,"
            " such as waving their claws or using physical displays to establish dominance. Most crabs reproduce by laying eggs, which are carried by females until they hatch into larvae. Crabs play essential roles in ecosystems as scavengers, predators, and prey."
            "\n\n\nBehavior of Crabs\n\n"
            "Crabs exhibit a variety of behaviors that are influenced by their environment, social interactions, and survival needs. One of the most notable behaviors is their sideways walking due to the structure of their legs, which allows them to move quickly, especially when evading predators."
            " Crabs are generally territorial and will defend their burrows or feeding areas aggressively, often using their large claws for combat with rivals. They also use their pincers for communication, such as waving them to signal threats or to attract mates."
            "\n\nMany crabs are nocturnal, emerging at night to forage for food, while others are active during the day. Their feeding behavior is opportunistic, as they scavenge for decaying organic material, hunt for smaller prey, or graze on plants, depending on their species. Crabs are also known"
            " for their burrowing behavior, digging and creating shelters in sandy or muddy areas to protect themselves from predators and environmental stress."
            "\n\nIn terms of mating behavior, male crabs often engage in displays of strength, using their large claws to attract females or deter other males."
            " Once a female is fertilized, she carries the eggs in a specialized pouch until they hatch. Crabs also have a unique defensive behavior in which they can shed limbs (autotomy) to escape from predators, and the lost limb will regenerate over time. Additionally, crabs can communicate"
            " through chemical signals or body postures, especially in social species where multiple crabs share the same environment, such as in mudflats or coastal habitats."
            "\n\n\nDiet\n\n"
            "Crabs are omnivorous and have a varied diet that includes both plant and animal matter. They feed on a wide range of food sources, depending on the species and their habitat. Common foods include algae, small fish, mollusks, snails, and worms. Many crabs are also scavengers,"
            " feeding on detritus or decaying organic material they find on the ocean floor, in muddy areas, or along coastal shores. Some crabs, like the fiddler crab, primarily consume plant material, such as seaweed and seagrass, while others, like the coconut crab, may also feed on fruits and leaves."
            " Certain species, such as the cancer crab, are more carnivorous, actively hunting for smaller crabs, shellfish, and even dead animals. Crabs use their powerful claws to break open shells and capture prey, and they may scavenge in groups, especially in coastal habitats where food is abundant."
            "\n\n\nHabitat\n\n"
            "Crabs are a diverse group of crabs that live primarily in marine environments, such as coastal waters, beaches, mangroves, rocky shores, and coral reefs. These crabs are typically adapted to life in the sea, with species found at various depths,"
            " from shallow waters to deeper ocean floors. Sea crabs are omnivores and feed on a wide range of materials, including algae, mollusks, smaller fish, and decaying organic matter. "
            "\n\nThey often seek shelter in burrows, crevices, or under rocks to avoid predators and the harsh conditions of the intertidal zone. Some species of sea crabs, like the blue crab and stone crab, are known for their strong claws used to catch prey and defend themselves."
            " Sea crabs have specialized adaptations for life in saltwater, such as gills for breathing and a hard exoskeleton to protect them from physical threats. They also exhibit behaviors such as mating rituals, territorial defense, and burrowing for shelter. Sea crabs play"
            " important roles in marine ecosystems, acting as scavengers, predators, and prey for larger animals."
            "\n\n\n",

            #Lobster
            "Lobster":
            "Lobsters are large marine crustaceans with tough exoskeletons and distinctive large claws, one often larger than the other. They have ten limbs, including eight walking legs and two antennae for sensing their surroundings."
            " Found in cold ocean waters, lobsters inhabit rocky seabeds and crevices, where they seek shelter. As omnivores, they feed on fish, mollusks, and detritus. Lobsters communicate using pheromones and physical gestures,"
            " especially during mating and territorial disputes. They molt to grow, and females carry fertilized eggs until they hatch into larvae. Lobsters are important in marine ecosystems and valued for their meat."
            "\n\n\nBehavior of Lobster\n\n"
            "Lobsters are primarily solitary and territorial creatures, often defending their shelters or burrows aggressively from other lobsters or predators. They communicate through pheromones and physical gestures, such as claw waving and posturing,"
            " especially during mating or territorial disputes. Lobsters are nocturnal hunters, emerging at night to forage for food, which includes fish, mollusks, and detritus."
            "\n\nLobsters are primarily solitary and territorial creatures, often defending their shelters or burrows aggressively from other lobsters or predators."
            " They communicate through pheromones and physical gestures, such as claw waving and posturing, especially during mating or territorial disputes. Lobsters are nocturnal"
            " hunters, emerging at night to forage for food, which includes fish, mollusks, and detritus."
            "\n\n\nDiet\n\n"
            "Lobsters are omnivores with a varied diet that includes fish, mollusks, crustaceans, worms, and detritus. They are opportunistic feeders, scavenging the ocean floor for food, and will eat almost anything they can find, including dead animals."
            " Their large claws are used to catch prey, break open shells, and defend against threats. Lobsters also feed on algae and sea plants in some cases, depending on the availability of food in their environment. Their diet helps maintain their energy for growth, molting, and reproduction."
            "\n\n\nRole in Ecosystem\n\n"
            "Lobsters play a crucial role in marine ecosystems as both predators and scavengers. As predators, they help control populations of smaller fish, mollusks, and other crustaceans, maintaining a balance in the food chain."
            " They are also important scavengers, feeding on dead organic matter, which helps break down and recycle nutrients back into the ecosystem. Lobsters are prey for a variety of marine animals, including fish, seals, and octopuses,"
            " making them a key part of the food web. Additionally, by creating and maintaining burrows and shelters, they provide habitats for other marine species, contributing to the biodiversity of their environment."
            "\n\n\nHabitat\n\n"
            "Lobsters primarily inhabit cold, deep ocean waters, typically found in rocky seabeds, muddy bottoms, and crevices along the coast. They prefer sheltered areas such as burrows, under rocks, or cavities in the seafloor where they can hide from predators and find food."
            " Lobsters are commonly found in temperate and subarctic regions, and some species live at depths ranging from shallow coastal waters to deeper ocean floors. They thrive in environments with stable temperatures and ample hiding places, as well as areas rich in food sources like fish, mollusks, and detritus."
            "\n\n\n",

            #Shrimp
            "Shrimp":
            "Shrimp are small, marine crustaceans belonging to the order Decapoda, known for their long, slender bodies, large antennae, and swimmerets used for swimming."
            " Their bodies are segmented into three parts: the head, thorax, and abdomen, and they have a flexible exoskeleton that requires molting as they grow. Shrimp typically have ten limbs,"
            " including eight walking legs and two long antennae for sensory functions. They vary in size, ranging from a few millimeters to over a foot long, and their color can range from transparent to white,"
            " pink, or brown, sometimes changing to blend with their environment. With compound eyes mounted on stalks, shrimp have a wide range of vision to detect predators and prey."
            "\n\nMost shrimp are omnivores, feeding on plant matter, plankton, detritus, and small animals, while some species are carnivorous or scavengers."
            " They inhabit diverse environments such as coastal waters, mangroves, coral reefs, and the deep sea, often taking shelter in burrows or under rocks."
            " Shrimp reproduce by laying eggs, and many species exhibit sexual dimorphism. They are known for their rapid tail flip swimming, used to escape predators, but can also crawl along the seafloor."
            " Shrimp play a vital role in marine ecosystems as both prey and predators, contributing to nutrient cycling and the food chain."
            "\n\n\nBehavior of Shrimp\n\n"
            "Shrimp exhibit a range of behaviors that help them survive in their environments. They are generally nocturnal, becoming more active during the night when they forage for food. Shrimp are social animals,"
            " often found in groups, though the size and structure of these groups can vary by species. They are scavengers and omnivores, feeding on a wide range of materials, including detritus, plankton, and small fish."
            " Some species also engage in burrowing to create shelter, while others may hide under rocks or within coral reefs to protect themselves from predators."
            "\n\nIn terms of movement, shrimp are known for their rapid tail flip, a quick escape response to avoid danger, allowing them to swim backward at high speeds. This behavior helps them evade predators like fish, birds, and larger marine animals."
            " During mating seasons, shrimp may exhibit courtship behaviors, with males using visual signals or physical gestures to attract females. Additionally, some shrimp species, such as the mantis shrimp, are highly territorial"
            " and will defend their burrows or shelters from other animals. Overall, shrimp display a variety of behaviors aimed at survival, feeding, reproduction, and avoiding predation."
            "\n\n\nDiet\n\n"
            "Shrimp are omnivores and have a varied diet that depends on their environment. They typically feed on detritus (dead organic matter), plankton, algae, and small invertebrates, including worms and other crustaceans."
            " Some species also consume small fish and benthic organisms found on the seafloor. Shrimp are scavengers, often foraging for leftover food from other animals or feeding on decaying matter, helping to clean the ocean floor."
            " Their diet helps to maintain the balance of nutrients in the ecosystem, and they can adjust their feeding habits based on the availability of food in their habitat. Some species, like mantis shrimp, may also eat larger prey, such as mollusks or other crustaceans, using their powerful claws to break open shells."
            "\n\n\nRole in Ecosystem\n\n"
            "Shrimp play a crucial role in marine ecosystems as both prey and predators. As scavengers, they help clean the ocean floor by consuming decaying organic matter, dead animals, and detritus, which contributes to nutrient recycling."
            " This process aids in maintaining the health of the ecosystem by ensuring that nutrients are returned to the environment. As predators, shrimp feed on plankton, small invertebrates, and fish larvae, helping regulate the populations of these species and maintaining balance in the food web."
            "\n\nShrimp are also an important food source for a variety of larger predators, including fish, birds, and marine mammals. In addition, they contribute to biodiversity by creating habitats for other organisms, such as by burrowing into the seafloor, which can provide shelter for smaller creatures."
            " Through these roles, shrimp help maintain the stability and health of aquatic ecosystems."
            "\n\n\nHabitat\n\n"
            "Shrimp inhabit a wide range of environments, primarily in marine ecosystems, though some species can also be found in freshwater habitats. They are commonly found in coastal waters, including mangroves, seagrass beds, and coral reefs, where they seek shelter and find abundant food."
            " Some shrimp species live in deeper ocean waters, often on the seafloor or in muddy or sandy bottoms. They prefer shallow waters, but certain species can thrive at depths of several hundred meters."
            "\n\nMany shrimp species burrow into the substrate or hide under rocks, corals, or within crevices to protect themselves from predators. Shrimp are also found in estuaries, where freshwater meets saltwater, and some species, like the prawn, migrate between fresh and saltwater environments during different life stages."
            " Their habitats provide both food sources and protection, which are essential for survival."
            
        }
           
        info_text = f"Species: {species}\n\n{species_info.get(species, 'No information available.')}"
        self.info_label.config(text=info_text)


    def create_threats_tab(self):
        title = tk.Label(self.threats_tab, text="Environmental Threats", font=("Helvetica", 17, "bold"))
        title.pack(pady=20)

        scrollable_frame = self.create_scrollable_frame(self.threats_tab)
        

        threats = {
            "1. Plastic Pollution": "Millions of tons of plastic waste end up in the ocean each year, threatening marine animals who may ingest it or become entangled. It also disrupts ecosystems.",
            "2. Chemical Pollution": "Toxic chemicals such as pesticides, heavy metals, and industrial waste runoff into oceans, poisoning marine life and destroying habitats.",
            "3. Climate Change": "Rising sea temperatures and ocean acidification caused by increased carbon emissions harm coral reefs, disrupt food chains, and threaten species that rely on stable environments.",
            "4. Overfishing": "Overfishing depletes fish stocks, disrupts marine food chains, and damages sensitive ecosystems like coral reefs, putting many species at risk of extinction.",
            "5. Loss of Habitat": "Coastal development, dredging, and destructive fishing practices damage vital habitats like coral reefs, mangroves, and seagrass beds that support marine biodiversity.",
            "6. Ocean Noise Pollution": "Increased ship traffic, industrial activities, and naval operations generate loud sounds that interfere with marine animals' communication, navigation, and mating.",
            "7. Invasive Species": "Non-native species introduced through human activity can outcompete native species, leading to ecological imbalances and threatening biodiversity."        
            
            }

        for threat, description in threats.items():
            label = tk.Label(scrollable_frame, text=f"{threat}: {description}", wraplength=1000, justify="left")
            label.pack(pady=10, anchor="w", padx=10)

    def create_tips_tab(self):
        title = tk.Label(self.tips_tab, text="Conservation Tips", font=("Helvetica", 17, "bold"))
        title.pack(pady=20)

        tips = [
            "1.) Reduce Plastic Usage: Avoid single-use plastics like straws, bags, and bottles to prevent marine animals from ingesting or getting entangled in them.",
            "2.) Support Sustainable Seafood: Choose seafood that is sustainably sourced to help protect fish populations and marine ecosystems from overfishing.",
            "3.) Participate in Beach Cleanups: Join or organize beach cleanups to remove trash that can harm marine creatures and ecosystems.",
            "4.) Minimize Chemical Use: Use eco-friendly cleaning products and avoid pesticides that can run off into the ocean and damage marine life.",
            "5.) Conserve Water: Reducing water consumption helps prevent runoff that can pollute oceans, affecting marine plants and animals.",
            "6.) Protect Marine Habitats: Be mindful of coral reefs, seagrasses, and mangroves, which are vital for marine biodiversity, and avoid activities that disturb these areas.",
            "7.) Raise Awareness: Educate others about marine conservation efforts and the importance of protecting our oceans and the creatures within them."
        ]

        for tip in tips:
            label = tk.Label(self.tips_tab, text=f"{tip}", wraplength=900, justify="left")
            label.pack(pady=10, anchor="w", padx=15)

    def create_learning_tab(self):
        title = tk.Label(self.learning_tab, text="Interactive Learning", font=("Helvetica", 17, "bold"))
        title.pack(pady=20)

        quiz_button = ttk.Button(self.learning_tab, text="Take a Quiz", command=self.start_quiz)
        quiz_button.pack(pady=5)

        fun_fact_label = tk.Label(self.learning_tab, text=
        "Fun Facts:\n\n"
        "Did you know coral reefs support over 25% of marine life?\n\n" 
        "Algae is actually the plural form of the word alga, which means a single plant-like organism. \n\n"
        "Octopuses have three hearts and blue blood! They are also incredibly intelligent, capable of solving puzzles and even using tools.\n\n"
        "Some shark species, like the great white shark, need to keep swimming continuously to breathe, as movement helps water flow over their gills.",
                                  wraplength=700, justify="left")
        fun_fact_label.pack(pady=10)

    def start_quiz(self):
        quiz_window = tk.Toplevel(self.master)
        quiz_window.title("Marine Life Quiz")

        # Variables to store the selected answers
        answers = {}

        # First question (Shrimp)
        question_label1 = tk.Label(quiz_window, text="What is a primary role of shrimp in marine ecosystems?", font=("Helvetica", 14))
        question_label1.pack(pady=20)

        def quiz1(selected_answer):
            answers["question1"] = selected_answer

        # First multiple choice options
        options1 = [
            ("A) They are top predators in the food chain.", "A"),
            ("B) They contribute to nutrient cycling and are part of the food chain.", "B"),
            ("C) They primarily feed on other shrimp.", "C"),
            ("D) They can survive in freshwater environments.", "D")
        ]

        for text, value in options1:
            button = ttk.Button(quiz_window, text=text, command=lambda v=value: quiz1(v))
            button.pack(fill=tk.X, pady=5)

        # Second question (Seals)
        question_label2 = tk.Label(quiz_window, text="How do seals primarily swim?", font=("Helvetica", 14))
        question_label2.pack(pady=10)

        def quiz2(selected_answer):
            answers["question2"] = selected_answer

        # Second multiple choice options
        options2 = [
            ("A) They swim using their front flippers.", "A"),
            ("B) They use their rear flippers, similar to a fish's tail.", "B"),
            ("C) They cannot swim.", "C"),
            ("D) They use a snake-like motion to propel themselves.", "D")
        ]

        for text, value in options2:
            button = ttk.Button(quiz_window, text=text, command=lambda v=value: quiz2(v))
            button.pack(fill=tk.X, pady=5)

        # Third question (Seals)
        question_label3 = tk.Label(quiz_window, text="What is a key characteristic that differentiates seagrasses from seaweeds?", font=("Helvetica", 14))
        question_label3.pack(pady=20)

        def quiz3(selected_answer):
            answers["question3"] = selected_answer

        # Second multiple choice options
        options3 = [
            ("A) Seagrasses are plants with roots, stems, and leaves, while seaweeds lack these structures.", "A"),
            ("B) Seagrasses live in freshwater environments, while seaweeds live in saltwater.", "B"),
            ("C) Seagrasses do not produce flowers or seeds, unlike seaweeds.", "C"),
            ("D) Seagrasses are only found in tropical waters, while seaweeds are found in polar regions.", "D")
        ]

        for text, value in options3:
            button = ttk.Button(quiz_window, text=text, command=lambda v=value: quiz3(v))
            button.pack(fill=tk.X, pady=3)

        # Button to show results
        def show_results():
            correct_answers = {
                "question1": "B",
                "question2": "B",
                "question3": "A"
            }

            results_text = "Quiz Results:\n\n"

            for question, correct_answer in correct_answers.items():
                selected_answer = answers.get(question, "Not Answered")
                results_text += f"{question.replace('question', 'Question ')}: "
                if selected_answer == correct_answer:
                    results_text += f"Correct (Your answer: {selected_answer})\n"
                else:
                    results_text += f"Incorrect (Your answer: {selected_answer})\n"

            messagebox.showinfo("Quiz Results", results_text)

        results_button = ttk.Button(quiz_window, text="Show Results", command=show_results)
        results_button.pack(pady=10)

        # Add a close button to the quiz window
        close_button = ttk.Button(quiz_window, text="Close", command=quiz_window.destroy)
        close_button.pack(pady=5)


if __name__ == "__main__":
    master = tk.Tk()
    app = EcoSeasApp(master)  
    master.mainloop()  
