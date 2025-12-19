import sys

try:
    from fpdf import FPDF
except ImportError:
    print("\n---------------------------------------------------------")
    print("ERROR: The module 'fpdf' is missing.")
    print("Please install it using the following command in your terminal:")
    print("pip install fpdf")
    print("---------------------------------------------------------\n")
    sys.exit(1)

class WenzkeCV(FPDF):
    def header(self):
        self.set_fill_color(60, 60, 60)
        self.rect(0, 0, 70, 297, 'F')

        if self.page_no() == 1:
            self.set_xy(75, 20)
            self.set_font('Helvetica', 'B', 24)
            self.set_text_color(0)
            self.cell(0, 10, 'MILAN BERGER', border=0, align='L', new_x="LMARGIN", new_y="NEXT")
            self.set_xy(75, 30)
            self.set_font('Helvetica', '', 12)
            self.set_text_color(100)
            self.cell(0, 8, 'Principal Solution Architect & Security Expert', border=0, align='L', new_x="LMARGIN", new_y="NEXT")

    def footer(self):
        self.set_y(-15)
        self.set_x(70)
        self.set_font('Helvetica', '', 8)
        self.set_text_color(150)
        self.cell(0, 10, f'Seite {self.page_no()}', border=0, align='R', new_x="RIGHT", new_y="TOP")

    def draw_sidebar_content(self, certs, languages):
        self.set_y(50)
        self.set_left_margin(5)
        self.set_right_margin(145)
        self.set_text_color(255, 255, 255)

        # CONTACT
        self.set_font('Helvetica', 'B', 11)
        self.set_x(5)
        self.cell(60, 8, "KONTAKT", border=0, align='L', new_x="LMARGIN", new_y="NEXT")    
        self.set_font('Helvetica', '', 9)
        self.set_x(5)
        self.multi_cell(60, 5, "Bunzlauer Straße 61\n90473 Nürnberg", align='L')
        self.ln(8)

        # lang
        self.set_font('Helvetica', 'B', 11)
        self.set_x(5)
        self.cell(60, 8, "SPRACHEN", border=0, align='L', new_x="LMARGIN", new_y="NEXT")
        self.set_font('Helvetica', '', 9)
        for lang in languages:
            self.set_x(5)
            self.cell(60, 5, lang, border=0, align='L', new_x="LMARGIN", new_y="NEXT")
        self.ln(8)

        # certs
        self.set_font('Helvetica', 'B', 11)
        self.set_x(5)
        self.cell(60, 8, "ZERTIFIKATE", border=0, align='L', new_x="LMARGIN", new_y="NEXT")
        self.set_font('Helvetica', '', 8)
        for cert in certs:
            self.set_x(5)
            self.multi_cell(60, 4, f"- {cert}", align='L')
            self.ln(1)
        self.ln(5)

    def section_title(self, title):
        self.ln(5)
        self.set_x(75)
        self.set_font('Helvetica', 'B', 12)
        self.set_text_color(30, 30, 30)
        self.cell(0, 8, title.upper(), border=0, align='L', new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(200)
        self.line(75, self.get_y(), 200, self.get_y())
        self.ln(5)

    def job_entry(self, date, company, role, details):
        self.set_x(75)
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(0)
        self.cell(35, 5, date, border=0, align='L', new_x="RIGHT", new_y="TOP")

        # Company
        self.set_font('Helvetica', 'B', 11)
        self.cell(0, 5, company, border=0, align='L', new_x="LMARGIN", new_y="NEXT")

        # Role
        self.set_x(110)
        self.set_font('Helvetica', 'I', 10)
        self.set_text_color(50)
        self.cell(0, 5, role, border=0, align='L', new_x="LMARGIN", new_y="NEXT")

        # Details
        self.ln(2)
        self.set_font('Helvetica', '', 10)
        self.set_text_color(30)
        for line in details:
            self.set_x(110)
            self.multi_cell(0, 5, f"- {line}", align='L')
        self.ln(4)

    def skill_block(self, category, items):
        self.set_x(75)
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(0)
        self.cell(40, 5, category + ":", border=0, align='L', new_x="RIGHT", new_y="TOP")
        self.set_font('Helvetica', '', 10)
        self.set_text_color(50)
        self.multi_cell(0, 5, items, align='L')
        self.ln(1)

certs_list = [
    "LPT (Licensed Penetration Tester)",
    "CEH (Certified Ethical Hacker)",
    "ECSA (Security Analyst)",
    "ITIL Foundation v4",
    "Splunk Certified User",
    "Ausbildereignung (IHK)"
]

langs_list = [
    "Deutsch (Muttersprache)",
    "Englisch (Verhandlungssicher)"
]

summary = (
    "Erfahrener Technical Lead und Solution Architect. Kombination aus tiefer technischer "
    "Expertise (Linux, K8s, Security) und C-Level Management-Erfahrung. "
    "Fokus auf Managed Services und Prozessdigitalisierung."
)

pdf = WenzkeCV()
pdf.set_auto_page_break(auto=True, margin=15)

pdf.add_page()
pdf.draw_sidebar_content(certs_list, langs_list)

pdf.set_left_margin(75)
pdf.set_right_margin(10)
pdf.set_y(45)

pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(50)
pdf.multi_cell(0, 5, summary, align='L')
pdf.ln(5)

# experience
pdf.section_title("Berufserfahrung")

# Adesso
pdf.job_entry("04.2024 - heute", "Adesso as a service GmbH", "Principal Solution Architect & Teamlead", [
    "Technical Lead Managed Service Infrastrukturen",
    "Fachliche Führung & Architekturverantwortung",
    "Tech Stack: Linux, K8s, Docker, DBs"
])

# Pharmastore
pdf.job_entry("04.2021 - heute", "Pharmastore GmbH", "Stellvertretender Geschäftsführer", [
    "Gesamtverantwortung IT-Modernisierung & Digitalisierung",
    "Einführung Topix ERP, Shopware, Zeiterfassung",
    "Operative Teamführung & Prozessoptimierung"
])

# SVA
pdf.job_entry("01.2018 - 03.2024", "System Vertrieb Alexander", "Big Data / Linux Systems Engineer", [
    "Betrieb heterogener Linux- & Hadoop-Cluster",
    "Aufbau Datamesh & Docker-Umgebungen",
    "Consulting & Koordination"
])

# Diehl
pdf.job_entry("08.2015 - 12.2017", "Diehl Connectivity Solutions", "Linux Systems Engineer", [
    "Aufbau B2B 3rd Level Customer Support",
    "Planung Cloud Backend & CERT Mitgliedschaft"
])

# Nureg
pdf.job_entry("01.2015 - 04.2015", "Nureg AG", "Linux Systems Engineer", [
    "Konfiguration Linux-Infrastruktur",
    "Umsetzung Sicherheitsmaßnahmen"
])

# QSC
pdf.job_entry("11.2006 - 12.2014", "QSC AG", "System Engineer / IT Security", [
    "Full-Managed Support & Security Audits (ISO 27001)",
    "Technische Ausbildung von Azubis"
])

# hard break to page 2
pdf.add_page() 
pdf.set_y(20) 

# skills
pdf.section_title("Fachkenntnisse & Stack")
pdf.skill_block("Container", "Docker (Enterprise, Swarm), Ansible, Kubernetes basics")
pdf.skill_block("OS", "Linux Expert (RHEL, SLES, Debian, Ubuntu), Unix")
pdf.skill_block("Data/DB", "Cloudera, Kafka, MariaDB, Postgres, Splunk")
pdf.skill_block("Security", "Nessus, OpenVAS, metasploit, rfid/nfc, ISO 27001")
pdf.skill_block("Web/Tools", "Apache, Nginx, CheckMK, Nagios, Wireshark, Jira")

# Selected Projects
pdf.ln(5)
pdf.section_title("Ausgewählte Projekte")
pdf.job_entry("Laufend", "Managed Services (Adesso)", "Lead Architect", [
    "Konzeption hochverfügbarer K8s-Umgebungen",
    "Prozessoptimierung Datenanalyse"
])

pdf.job_entry("Laufend", "Digitalisierung (Pharmastore)", "Projektleitung", [
    "Einführung Warenwirtschaft (Topix) & Webshop (Shopware)",
    "Modernisierung Mailserver & Security"
])

pdf.job_entry("2022 - 2024", "Big Data Ops (Automotive)", "Ops Engineer", [
    "Full Managed Service für Big Data Cluster",
    "Tech: SuSE, Kafka, Trino, Minio, Spark"
])

pdf.output("Milan_Berger_CV.pdf")
print("PDF created successfully")
