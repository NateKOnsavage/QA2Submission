#put this in gemenai to start project: iwanoseapyhonscpttocreatteadatabasefile.inthisdatabasefile.thereneedstobe4tables.the  tables are Ds3850,IntroToTheater,OrgBehavior,DatabaseManagement.makethedatabasefilenamed"nakonsavag42QuizDB.db".ineachogfthesetables:iwantalistof10multipple choise qestiions.The qestons shouldrelate to the course. 
#after making he database file,committ it to git hub
#make a databse tester



import sqlite3

# Define the database file name
DB_NAME = "nakonsavag42QuizDB.db"

# Data structure for questions: (question, option_a, option_b, option_c, option_d, correct_answer)
# The correct answer should match the letter of one of the options (A, B, C, or D).

# Assuming DS3850 is a course about Industrial Control Systems/Cyber Systems based on search results.
ds3850_questions = [
    ("What does SCADA stand for in the context of Industrial Control Systems?", "Supervisory Control and Data Administration", "Site Control And Data Acquisition", "Supervisory Control and Data Acquisition", "Systematic Control and Data Analysis", "C"),
    ("Which component of a SCADA system communicates directly with field devices like sensors and actuators?", "Master Terminal Unit (MTU)", "Human-Machine Interface (HMI)", "Remote Terminal Unit (RTU)", "Data Logger", "C"),
    ("Which of the following is NOT a typical benefit of industrial cyber systems?", "Efficient and scalable production", "Optimized performance", "Improved machine intelligence", "Decreased system complexity and ease of upgrades", "D"),
    ("What is the primary function of a Programmable Logic Controller (PLC)?", "To manage enterprise resource planning", "To replace traditional relays for controlling manufacturing processes", "To provide a graphical interface for operators", "To handle long-term data archival", "B"),
    ("Which layer of the Purdue Model for Industrial Control Systems is the Enterprise network?", "Level 0", "Level 3", "Level 4", "Level 5", "C"),
    ("A **denial of service (DoS)** attack on an industrial control system aims to:", "Steal proprietary blueprints", "Disrupt the availability of the system's function", "Modify process control values secretly", "Gain remote access to the HMI", "B"),
    ("What is an inherent security challenge in many legacy Industrial Control Systems (ICS)?", "They use modern, secure operating systems", "They are often air-gapped from all networks", "Remote devices are often hard to upgrade or patch", "They exclusively use encrypted communication protocols", "C"),
    ("In Industrial Internet of Things (IIoT), what term describes a system where physical industrial assets are digitally twinned?", "Digital Marketing", "Cyber-Physical System (CPS)", "Business Intelligence (BI)", "Cloud Computing", "B"),
    ("What type of malicious software encrypts a victim's files, often targeting ICS systems, and demands a ransom?", "Adware", "Spyware", "Ransomware", "Worm", "C"),
    ("Which industrial communication protocol is a common target for cyber security vulnerabilities?", "HTTPS", "Ethernet/IP", "SSH", "SFTP", "B"),
]

intro_to_theater_questions = [
    ("The word 'Theatre' comes from the Greek word **'Theatron'** which literally means:", "Sleeping place", "Seeing place", "Walking place", "Sitting place", "B"),
    ("Who is considered the principal character in a play, the one the story is primarily about?", "Antagonist", "Protagonist", "Playwright", "Understudy", "B"),
    ("The detailed information revealing the facts of the plot, typically at the beginning of a play, is called the:", "Climax", "Exposition", "Theme", "Diction", "B"),
    ("Which element of a dramatic structure, according to Aristotle, is NOT one of the six key elements (Plot, Character, Thought, Diction, Music, Spectacle)?", "Plot", "Character", "Situation", "Spectacle", "C"),
    ("Plays in Ancient Greece were first performed as part of a festival honoring which god?", "Zeus", "Athena", "Dionysus", "Apollo", "C"),
    ("What is the term for the lines or signals that alert an actor to be ready to speak, enter, or exit?", "Subtext", "Dialogue", "Theme", "Cue", "D"),
    ("A performer prepared to take over an important role should the main actor miss a performance is known as the:", "Director", "Set Designer", "Understudy", "Grip", "C"),
    ("Which term is used for a scene performed without a written script, focusing on spontaneous action and dialogue?", "Pantomime", "Hot seating", "Improvisation", "Monologue", "C"),
    ("Major divisions of a play, often separated by an intermission, are called:", "Scenes", "Beats", "Acts", "Pages", "C"),
    ("The visual elements of a play, including scenery, costumes, and lighting, are collectively known as:", "Diction", "Spectacle", "Theme", "Thought", "B"),
]

org_behavior_questions = [
    ("Organizational Behavior (OB) is primarily the study of what in an organization?", "Financial accounting and auditing", "Individual, group, and organizational structure's impact on behavior", "The chemistry and biology of human resources", "Supply chain and logistics management", "B"),
    ("Which of the following is NOT one of the 'Big Five' personality dimensions?", "Conscientiousness", "Neuroticism (Emotional Stability)", "Locus of Control", "Extraversion", "C"),
    ("Which term describes the degree to which employees identify with and are emotionally committed to their work?", "Job enrichment", "Role perception", "Employee engagement", "Values congruence", "C"),
    ("In the context of attribution theory, if everyone who is faced with a similar situation responds in the same way, the behavior shows high:", "Distinctiveness", "Flexibility", "Consistency", "Consensus", "D"),
    ("The process where one attribute of a person or situation is used to develop an overall impression is known as the:", "Projection", "Stereotyping", "Halo effect", "Perceptual set", "C"),
    ("Direction, intensity, and persistence are the three dimensions of what key concept in OB?", "Ability", "Motivation", "Role perception", "Organizational culture", "B"),
    ("The belief that 'Might is right' is the motto of which Organizational Behavior model?", "Supportive Model", "Collegial Model", "Custodial Model", "Autocratic Model", "D"),
    ("Which theory explains how and why people react when they feel unfairly treated in comparison to others?", "Expectancy Theory", "Goal Setting Theory", "Equity Theory", "Reinforcement Theory", "C"),
    ("The concept that a whole is greater than the sum of its parts, often applied to team performance, is called:", "Presenteeism", "Performance efficiency", "Synergy", "Halo effect", "C"),
    ("What does **stereotyping** involve in perception?", "Assigning one's own personal attributes to others", "Using one trait to form an overall impression", "Judging an individual based on the group or category they belong to", "The tendency to find what you expected to find", "C"),
]

database_management_questions = [
    ("What does the acronym **DBMS** stand for?", "Database Modeling System", "Data Base Management Software", "Database Management System", "Data Binary Module System", "C"),
    ("Which SQL command is used to retrieve data from a database?", "INSERT", "UPDATE", "SELECT", "DELETE", "C"),
    ("Which of the following is a primary goal of **normalization** in a relational database?", "Increasing data access speed", "Minimizing data redundancy and dependency", "Improving data encryption", "Defining stored procedures", "B"),
    ("Which of the following keys is used to uniquely identify a record (tuple) in a table and cannot contain NULL values?", "Foreign Key", "Super Key", "Candidate Key", "Primary Key", "D"),
    ("What does the 'A' in the **ACID** properties of database transactions stand for?", "Association", "Aggregation", "Atomicity", "Availability", "C"),
    ("Which part of the DBMS architecture describes the data storage and access methods at the lowest level of abstraction?", "Logical Level", "View Level", "Conceptual Level", "Physical Level", "D"),
    ("The **WHERE** clause in a SELECT statement is used for what purpose?", "To group the result rows by a column", "To sort the result set in ascending or descending order", "To filter the records returned based on a specified condition", "To combine data from multiple tables", "C"),
    ("A **Foreign Key** in a relational database serves what primary purpose?", "To uniquely identify a row in its own table", "To enforce data encryption", "To establish a link and enforce referential integrity between two tables", "To speed up data retrieval", "C"),
    ("Which type of SQL command is used to modify the structure of the database, such as creating or dropping tables?", "DCL (Data Control Language)", "DML (Data Manipulation Language)", "TCL (Transaction Control Language)", "DDL (Data Definition Language)", "D"),
    ("What term refers to the number of tuples (rows) in a relation (table)?", "Degree", "Attribute", "Cardinality", "Domain", "C"),
]


def create_and_populate_db():
    """Connects to SQLite, creates tables, and inserts quiz data."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Define table schemas
        table_definitions = {
            "DS3850": ds3850_questions,
            "IntroToTheater": intro_to_theater_questions,
            "OrgBehavior": org_behavior_questions,
            "DatabaseManagement": database_management_questions,
        }

        # SQL for table creation and data insertion
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS {} (
            QuestionID INTEGER PRIMARY KEY AUTOINCREMENT,
            Question TEXT NOT NULL,
            OptionA TEXT NOT NULL,
            OptionB TEXT NOT NULL,
            OptionC TEXT NOT NULL,
            OptionD TEXT NOT NULL,
            CorrectAnswer TEXT NOT NULL -- A, B, C, or D
        );
        """
        
        insert_question_sql = """
        INSERT INTO {} (Question, OptionA, OptionB, OptionC, OptionD, CorrectAnswer)
        VALUES (?, ?, ?, ?, ?, ?);
        """

        # Create tables and insert data
        for table_name, questions in table_definitions.items():
            print(f"Processing table: {table_name}")
            
            # 1. Drop table if it exists (for easy re-run of the script)
            cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
            
            # 2. Create the table
            cursor.execute(create_table_sql.format(table_name))
            
            # 3. Insert the questions
            cursor.executemany(insert_question_sql.format(table_name), questions)
            
            # Check the count (optional)
            cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
            count = cursor.fetchone()[0]
            print(f"  -> Successfully inserted {count} records into {table_name}")

        # Commit changes and close connection
        conn.commit()
        print(f"\n✅ Database '{DB_NAME}' created and populated successfully!")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_and_populate_db()






