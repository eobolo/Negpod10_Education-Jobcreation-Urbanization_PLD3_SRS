#!/usr/bin/python3
"""testing the all-jobs.py
"""
"""
jobs = {
    'A': ['Accountant', 'Actor', 'Architect', 'Artist', 'Astronomer', 'Athlete'],
    'B': ['Baker', 'Barista', 'Bartender', 'Biologist', 'Bricklayer', 'Bus Driver'],
    'C': ['Carpenter', 'Cashier', 'Chef', 'Chemist', 'Civil Engineer', 'Cleaner'],
    'D': ['Dancer', 'Dentist', 'Designer', 'Detective', 'Doctor', 'Driver'],
    'E': ['Editor', 'Electrician', 'Engineer', 'Entertainer', 'Entrepreneur', 'Explorer'],
    'F': ['Farmer', 'Fashion Designer', 'Firefighter', 'Fisherman', 'Flight Attendant', 'Florist'],
    'G': ['Gardener', 'Geologist', 'Graphic Designer', 'Grocer', 'Guidance Counselor', 'Gymnast'],
    'H': ['Hairdresser', 'Historian', 'Housekeeper', 'HR Manager', 'Hydrologist', 'Hypnotherapist'],
    'I': ['Illustrator', 'Information Security Analyst', 'Interpreter', 'Investigator', 'IT Specialist'],
    'J': ['Janitor', 'Journalist', 'Judge', 'Jeweler', 'Jockey', 'Joiner'],
    'K': ['Kinesiologist', 'Kindergarten Teacher', 'Kiosk Attendant', 'Kitchen Staff', 'Knitter'],
    'L': ['Landscape Architect', 'Librarian', 'Lifeguard', 'Linguist', 'Locksmith', 'Lumberjack'],
    'M': ['Mail Carrier', 'Makeup Artist', 'Manager', 'Marine Biologist', 'Mathematician', 'Mechanic'],
    'N': ['Nanny', 'Navigator', 'Nurse', 'Nutritionist', 'Novelist', 'News Anchor'],
    'O': ['Occupational Therapist', 'Oceanographer', 'Office Clerk', 'Opera Singer', 'Optometrist'],
    'P': ['Painter', 'Paramedic', 'Pharmacist', 'Photographer', 'Physicist', 'Pilot'],
    'Q': ['Quality Control Inspector', 'Quarantine Officer', 'Quilter'],
    'R': ['Radiographer', 'Real Estate Agent', 'Receptionist', 'Research Scientist', 'Restaurateur'],
    'S': ['Sailor', 'Salesperson', 'Scientist', 'Sculptor', 'Security Guard', 'Singer'],
    'T': ['Tailor', 'Teacher', 'Technician', 'Translator', 'Truck Driver', 'Tour Guide'],
    'U': ['Umpire', 'Underwriter', 'Urologist', 'Urban Planner'],
    'V': ['Veterinarian', 'Video Game Developer', 'Vocal Coach', 'Volunteer'],
    'W': ['Waiter/Waitress', 'Web Developer', 'Welder', 'Writer'],
    'X': ['X-ray Technician', 'Xenobiologist', 'Xylophonist'],
    'Y': ['Yoga Instructor', 'Youth Counselor'],
    'Z': ['Zoologist', 'Zumba Instructor']
}
"""
write_json_file = __import__("all_jobs").write_json_file
read_json_file = __import__("all_jobs").read_json_file
data = read_json_file()
print(read_json_file())
