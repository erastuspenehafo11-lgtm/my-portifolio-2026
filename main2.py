"""
Portfolio — Group 3 | Documentation Lead
I3691CP Computer Programming I | UNAM JEDS Campus
Run:  flet run main.py
Web:  flet run --web main.py
"""
import os
import base64
import flet as ft

# ── Colour tokens (light blue + pink/purple pastel) ──────────────────────────
BG          = "#F0F4FF"          # soft blue-white page background
CARD        = "#FFFFFF"          # white cards
CARD2       = "#EEF2FF"          # very light blue card
BORDER_C    = "#C7D2FE"          # soft indigo border
BLUE        = "#6366F1"          # indigo primary
BLUE_DIM    = "#EEF2FF"          # light indigo bg
BLUE_DARK   = "#4338CA"          # darker indigo
AMBER       = "#EC4899"          # pink accent
AMBER_DIM   = "#FDF2F8"          # light pink bg
GREEN       = "#8B5CF6"          # purple
GREEN_DIM   = "#F5F3FF"          # light purple bg
PURPLE      = "#A855F7"          # vivid purple
PURPLE_DIM  = "#FAF5FF"          # light purple bg
ROSE        = "#F472B6"          # pink rose
ROSE_DIM    = "#FDF2F8"          # light rose bg
TEAL        = "#06B6D4"          # cyan
TEAL_DIM    = "#ECFEFF"          # light cyan bg
WHITE       = "#1E1B4B"          # dark text (inverted for light theme)
MUTED       = "#6B7280"          # muted text
MUTED2      = "#4B5563"          # slightly darker muted
NAV_BG      = "#FFFFFF"          # white nav bar

# ── Student info ──────────────────────────────────────────────────────────────
STUDENT_NAME     = "Erastus Penehafo"
STUDENT_NUMBER   = "224082833"
STUDENT_INITIALS = "EP"

def _load_photo(filename):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    try:
        with open(path, "rb") as f:
            return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()
    except Exception:
        return ""

PROFILE_PHOTO_SRC = _load_photo("photo.jpg")  # put photo.jpg in same folder

def _load_cert(filename):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    try:
        with open(path, "rb") as f:
            return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()
    except Exception:
        return ""

CERT_IMAGES = {
    "MATLAB_Onramp":                       _load_cert("MATLAB Onramp.jpg"),
    "Make_and_Manipulate_Matrices":        _load_cert("Make and Manipulate Matrices.jpg"),
    "Calculations_with_Vectors_and_Matrices": _load_cert("Calculations with Vectors and Matrices.jpg"),
    "Explore_Data_with_MATLAB_Plots":      _load_cert("Explore Data with MATLAB Plots.jpg"),
    "Simulink_Onramp":                     _load_cert("Simulink Onramp.jpg"),
    "Simulink_Fundamentals":               _load_cert("Simulink Fundamentals.jpg"),
    "Import_Data_from_Multiple_Files":     _load_cert("Import Data from Multiple Files.jpg"),
    "Statistics_Onramp":                   _load_cert("Statistics Onramp.jpg"),
}

COURSES = [
    {"name": "MATLAB Onramp",                       "date": "26 April 2026",  "key": "MATLAB_Onramp"},
    {"name": "Make and Manipulate Matrices",         "date": "26 April 2026", "key": "Make_and_Manipulate_Matrices"},
    {"name": "Calculations with Vectors & Matrices", "date": "26 April 2026", "key": "Calculations_with_Vectors_and_Matrices"},
    {"name": "Explore Data with MATLAB Plots",       "date": "26 April 2026", "key": "Explore_Data_with_MATLAB_Plots"},
    {"name": "Simulink Onramp",                      "date": "26 April 2026", "key": "Simulink_Onramp"},
    {"name": "Simulink Fundamentals",                "date": "29 April 2026", "key": "Simulink_Fundamentals"},
    {"name": "Import Data from Multiple Files",      "date": "29 April 2026", "key": "Import_Data_from_Multiple_Files"},
    {"name": "Statistics Onramp",                    "date": "29 April 2026", "key": "Statistics_Onramp"},
]

# ── Helpers ───────────────────────────────────────────────────────────────────
def tag(text, color=BLUE, bg=None):
    return ft.Container(
        ft.Text(text, size=9, color=color, weight=ft.FontWeight.BOLD,
                style=ft.TextStyle(letter_spacing=1.5)),
        bgcolor=bg or BLUE_DIM,
        padding=ft.Padding.symmetric(horizontal=10, vertical=4),
        border_radius=20,
        border=ft.Border.all(1, color),
    )

def glass_card(content, padding=20, glow=BLUE):
    return ft.Container(
        content=content,
        bgcolor=CARD,
        border_radius=16,
        padding=padding,
        border=ft.Border.all(1, BORDER_C),
        shadow=ft.BoxShadow(blur_radius=20, color=glow + "18",
                            offset=ft.Offset(0, 4)),
    )

def section_title(text):
    return ft.Row([
        ft.Container(width=3, height=18, bgcolor=BLUE, border_radius=2),
        ft.Text(text.upper(), size=10, color=BLUE, weight=ft.FontWeight.BOLD,
                style=ft.TextStyle(letter_spacing=2)),
    ], spacing=10)

def page_title(title, subtitle=""):
    return ft.Column([
        ft.Text(title, size=26, weight=ft.FontWeight.BOLD, color=WHITE),
        ft.Text(subtitle, size=12, color=MUTED) if subtitle else ft.Container(height=0),
    ], spacing=4)

def dot_line():
    return ft.Container(height=1, bgcolor=BORDER_C,
                        margin=ft.Margin.only(top=4, bottom=4))

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — TIMELINE  (dark cards, left timeline stripe)
# ══════════════════════════════════════════════════════════════════════════════
WEEKS = [
    {"week":"Week 1-2","phase":"Phase 0","color":BLUE,
     "title":"Group formation and documentation setup",
     "desc":"Joined Group 3 as Documentation Lead. Helped set up the project repository structure and created the initial README with all group member names, student numbers, roles, and the app description."},
    {"week":"Week 3-4","phase":"Phase 1","color":TEAL,
     "title":"Pitch preparation and idea documentation",
     "desc":"Contributed to preparing the three app ideas for the pitch session. Documented the problem statement, target users, core features, and technology plan. Attended the pitch session with Mr. Abisai."},
    {"week":"Week 5","phase":"Phase 2","color":PURPLE,
     "title":"SRS — Introduction and system overview",
     "desc":"Authored Section 1 (Introduction) and Section 2 (System Overview) of the SRS. Wrote the problem statement, scope, target user descriptions, and technology overview narrative."},
    {"week":"Week 6","phase":"Phase 2","color":AMBER,
     "title":"SRS — Functional requirements",
     "desc":"Documented all functional requirements in the SRS including acceptance criteria and technology service mappings. Ensured all requirements were specific, testable, and traceable."},
    {"week":"Week 7","phase":"Phase 2","color":GREEN,
     "title":"Requirements finalisation — constraints and use cases",
     "desc":"Formulated the system operational constraints, performance thresholds, and security parameters while charting the foundational use case flows for the SRS."},
    {"week":"Week 8","phase":"Phase 2","color":ROSE,
     "title":"SRS editorial review and submission",
     "desc":"Executed a comprehensive editorial review of the 10+ page SRS, pushed the verified file to /docs, and completed the UNAM portal submission ahead of the closing deadline."},
    {"week":"Week 9","phase":"Phase 3","color":BLUE,
     "title":"Figma user-flow analysis",
     "desc":"Analyzed early Figma user-flow iterations to confirm absolute architectural alignment with the established SRS boundaries."},
    {"week":"Week 10","phase":"Phase 3","color":TEAL,
     "title":"Wireframe structural audit",
     "desc":"Conducted a structural audit of the interactive wireframes, ensuring every single functional requirement had a dedicated user interface screen."},
    {"week":"Week 11","phase":"Phase 3","color":PURPLE,
     "title":"Written Design Rationale",
     "desc":"Maintained design compliance by authoring the 2-page Written Design Rationale, detailing layout logic, accessibility standards, and color palettes."},
    {"week":"Week 12","phase":"Phase 3","color":AMBER,
     "title":"Design folder pipeline and prototype notes",
     "desc":"Managed the design folder pipeline by exporting all high-fidelity screens as PNGs to /designs and drafting the team prototype walkthrough notes."},
    {"week":"Week 13","phase":"Phase 4","color":GREEN,
     "title":"Demo feedback and sprint backlog",
     "desc":"Captured and structured all technical recommendations from Mr. Abisai during the live progress demo to build the team final sprint backlog."},
    {"week":"Week 14","phase":"Phase 4","color":ROSE,
     "title":"User Manual and final submission",
     "desc":"Authored the mandatory 5-page User Operational Manual, synchronized minor requirement updates in the SRS, compiled individual team reports, and successfully verified the entire 7-item submission bundle before the absolute deadline."},
]

def timeline_view():
    items = []
    for i, w in enumerate(WEEKS):
        last = i == len(WEEKS) - 1
        items.append(ft.Row([
            # Left: timeline dot + line
            ft.Column([
                ft.Container(width=12, height=12, bgcolor=w["color"],
                             border_radius=6,
                             border=ft.Border.all(2, w["color"] + "80")),
                ft.Container(width=2, expand=True, bgcolor=BORDER_C,
                             margin=ft.Margin.only(left=5)) if not last
                else ft.Container(expand=True),
            ], spacing=0, horizontal_alignment=ft.CrossAxisAlignment.CENTER,
               width=20),
            # Right: content
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Container(
                            ft.Text(w["week"], size=10, color=w["color"],
                                    weight=ft.FontWeight.BOLD),
                            bgcolor=CARD2, border_radius=6,
                            padding=ft.Padding.symmetric(horizontal=8, vertical=3),
                            border=ft.Border.all(1, w["color"] + "50"),
                        ),
                        ft.Text(w["phase"], size=10, color=MUTED),
                    ], spacing=8),
                    ft.Text(w["title"], size=13, weight=ft.FontWeight.BOLD,
                            color=WHITE),
                    ft.Text(w["desc"], size=12, color=MUTED2),
                ], spacing=6),
                bgcolor=CARD,
                border_radius=12,
                padding=ft.Padding.symmetric(horizontal=16, vertical=14),
                border=ft.Border.all(1, BORDER_C),
                margin=ft.Margin.only(bottom=12 if not last else 0),
                expand=True,
            ),
        ], spacing=14, vertical_alignment=ft.CrossAxisAlignment.START))

    return ft.Column([
        ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Column([
                        page_title("Project Timeline", "My weekly contributions — Group 3"),
                    ], expand=True),
                    tag("WEEKLY LOG"),
                ], vertical_alignment=ft.CrossAxisAlignment.START),
                ft.Container(height=6),
                ft.Container(
                    ft.Row([
                        ft.Icon(ft.Icons.SCHOOL, color=MUTED, size=14),
                        ft.Text("UNAM JEDS | I3691CP | Mr. Mathew Abisai | 02 Mar - 13 Jun 2026",
                                size=11, color=MUTED, expand=True),
                    ], spacing=8),
                    bgcolor=CARD2, border_radius=8,
                    padding=ft.Padding.symmetric(horizontal=14, vertical=10),
                ),
            ], spacing=10),
            bgcolor=CARD, border_radius=16, padding=20,
            border=ft.Border.all(1, BORDER_C),
            shadow=ft.BoxShadow(blur_radius=20, color=BLUE+"18", offset=ft.Offset(0,4)),
        ),
        ft.Container(height=16),
        *items,
        ft.Container(height=20),
    ], spacing=0, scroll=ft.ScrollMode.AUTO, expand=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — GITHUB EVIDENCE
# ══════════════════════════════════════════════════════════════════════════════
def github_view():
    def load_img(filename):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        try:
            with open(path, "rb") as f:
                return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()
        except Exception:
            return ""

    commits_src = load_img("commits.jpg")

    def screenshot_card(title, subtitle, icon, img_src):
        return glass_card(ft.Column([
            ft.Row([
                ft.Container(ft.Icon(icon, color=BLUE, size=20),
                             width=40, height=40, bgcolor=BLUE_DIM,
                             border_radius=10, alignment=ft.Alignment(0,0)),
                ft.Column([
                    ft.Text(title, size=13, weight=ft.FontWeight.BOLD, color=WHITE),
                    ft.Text(subtitle, size=11, color=MUTED),
                ], spacing=2, expand=True),
            ], spacing=12),
            ft.Container(height=10),
            ft.Image(src=img_src, width=700, fit="contain") if img_src else
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.ADD_PHOTO_ALTERNATE, color=MUTED, size=32),
                    ft.Text("Put commits.jpg in the same folder as main.py",
                            size=11, color=MUTED, text_align=ft.TextAlign.CENTER),
                ], spacing=6, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                bgcolor=CARD2, border_radius=10,
                border=ft.Border.all(1, BORDER_C),
                padding=ft.Padding.symmetric(horizontal=20, vertical=30),
                alignment=ft.Alignment(0,0),
            ),
        ], spacing=0))

    impact_paras = [
        "The Safe Sphere application addresses a critical challenge in Metallurgical, Mining, and Civil Engineering industries: inadequate safety awareness and training before entering hazardous work environments. Many accidents occur because workers, students, and site visitors lack sufficient knowledge of workplace hazards and safety procedures. Safe Sphere helps bridge this gap by providing accessible safety education, training courses, quizzes, and progress tracking through a mobile platform.",
        "The application code enables users to register securely, access safety training content, complete assessments, and monitor their learning progress. These features ensure that users gain essential knowledge about workplace risks before entering mines, processing plants, construction sites, or industrial facilities. By tracking course completion and quiz performance, the system encourages continuous learning and verifies that users understand important safety concepts.",
        "The project documentation played an important role by clearly defining system requirements, user needs, functional features, and safety objectives. This ensured that the development team created a solution aligned with industry safety challenges and user expectations. Through its focus on prevention rather than reaction, Safe Sphere contributes to reducing workplace incidents, improving safety awareness, and promoting safer practices across Metallurgical, Mining, and Civil Engineering operations.",
    ]

    return ft.Column([
        ft.Container(
            content=ft.Row([
                page_title("GitHub Evidence", "Contributions and impact"),
                tag("GROUP 3"),
            ], vertical_alignment=ft.CrossAxisAlignment.START),
            bgcolor=CARD, border_radius=16, padding=20,
            border=ft.Border.all(1, BORDER_C),
            shadow=ft.BoxShadow(blur_radius=20, color=BLUE+"18", offset=ft.Offset(0,4)),
        ),
        ft.Container(height=16),
        section_title("Commit History"),
        ft.Container(height=8),
        screenshot_card("Commit History Screenshot", "Your GitHub account",
                        ft.Icons.COMMIT, commits_src),
        ft.Container(height=16),
        section_title("Impact Summary"),
        ft.Container(height=8),
        glass_card(ft.Column([
            ft.Row([
                ft.Container(ft.Icon(ft.Icons.BOLT, color=AMBER, size=18),
                             width=36, height=36, bgcolor=AMBER_DIM,
                             border_radius=10, alignment=ft.Alignment(0,0)),
                ft.Text("My Role and Impact", size=14,
                        weight=ft.FontWeight.BOLD, color=WHITE, expand=True),
            ], spacing=12),
            ft.Container(height=8),
            *[ft.Text(p, size=13, color=MUTED2, selectable=True) for p in impact_paras],
        ], spacing=10), glow=AMBER),
        ft.Container(height=20),
    ], spacing=10, scroll=ft.ScrollMode.AUTO, expand=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 3 — BLOG
# ══════════════════════════════════════════════════════════════════════════════
BLOG_POST = [
    {
        "label": "CONCEPT 1",
        "color": BLUE,
        "bg":    BLUE_DIM,
        "title": "Mobile Application Development with React Native",
        "body":  "Safe Sphere was developed as a mobile application using React Native. React Native allows developers to build cross-platform applications using JavaScript and a single codebase. This approach reduces development time and ensures that the application can be adapted for both Android and iOS devices in the future. React Native also provides reusable components, making the application easier to maintain and update.",
    },
    {
        "label": "CONCEPT 2",
        "color": PURPLE,
        "bg":    PURPLE_DIM,
        "title": "Firebase Authentication",
        "body":  "Firebase Authentication was selected to manage user registration and login. This service provides a secure method of authenticating users through email and password credentials. By using Firebase Authentication, user accounts are protected, and only authorized users can access safety courses, quizzes, and progress information. This improves the overall security and reliability of the application.",
    },
    {
        "label": "CONCEPT 3",
        "color": TEAL,
        "bg":    TEAL_DIM,
        "title": "Cloud Database Management with Firestore",
        "body":  "The application uses Firebase Firestore as its cloud database. Firestore stores user information, course content, quiz results, and progress records in collections and documents. This cloud-based approach ensures that data is available across devices and can be synchronized in real time. Firestore also provides scalability, allowing the application to support a large number of users without significant performance issues.",
    },
    {
        "label": "CONCEPT 4",
        "color": AMBER,
        "bg":    AMBER_DIM,
        "title": "Progress Tracking System",
        "body":  "A key feature of Safe Sphere is the ability to track user learning progress. The system records completed lessons, quiz scores, and course completion status. This enables users to monitor their learning journey and identify areas that require improvement. Progress tracking also encourages continuous engagement with safety training materials.",
    },
    {
        "label": "CONCEPT 5",
        "color": GREEN,
        "bg":    GREEN_DIM,
        "title": "Safety Awareness and Hazard Prevention",
        "body":  "The core concept behind Safe Sphere is prevention rather than reaction. The application provides educational content related to mining and industrial hazards, helping users understand potential risks before entering hazardous environments. By increasing safety awareness, the system contributes to reducing workplace accidents and promoting a stronger safety culture.",
    },
    {
        "label": "CONCEPT 6",
        "color": ROSE,
        "bg":    ROSE_DIM,
        "title": "User-Centred Design",
        "body":  "The application was designed with usability in mind. The interface is simple, intuitive, and suitable for users with basic smartphone skills. Clear navigation, readable content, and straightforward functionality ensure that users can easily access training materials and track their progress without requiring technical expertise.",
    },
    {
        "label": "CONCLUSION",
        "color": BLUE,
        "bg":    BLUE_DIM,
        "title": "Confidence in Concepts",
        "body":  "Through the development of Safe Sphere, I gained confidence in several important software engineering concepts, including mobile application development, database management, user authentication, cloud computing, and user-centred design. Understanding how these technologies work together has strengthened my ability to develop practical software solutions that address real-world challenges in mining and industrial safety.",
    },
]

def blog_view():
    import os, shutil
    import flet_video as fv

    src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "video.mp4")
    assets_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
    dst_path = os.path.join(assets_dir, "video.mp4")

    video_available = False
    if os.path.exists(src_path):
        os.makedirs(assets_dir, exist_ok=True)
        if not os.path.exists(dst_path):
            shutil.copy2(src_path, dst_path)
        video_available = True

    if video_available:
        video_widget = fv.Video(
            playlist=[fv.VideoMedia(dst_path)],
            show_controls=True,
            autoplay=False,
            width=680,
            height=383,
        )
        video_content = ft.Column([
            ft.Row([
                ft.Container(
                    ft.Icon(ft.Icons.PLAY_CIRCLE, color=BLUE, size=18),
                    bgcolor=BLUE_DIM, border_radius=20,
                    padding=ft.Padding.symmetric(horizontal=8, vertical=8),
                ),
                ft.Column([
                    ft.Text("Safe Sphere — Semester Contribution Video", size=13,
                            weight=ft.FontWeight.BOLD, color=WHITE),
                    ft.Text("Plays directly below", size=11, color=MUTED),
                ], spacing=2, expand=True),
                ft.Container(
                    ft.Text("1:30 MAX", size=9, color=AMBER,
                            weight=ft.FontWeight.BOLD),
                    bgcolor=AMBER_DIM, border_radius=6,
                    padding=ft.Padding.symmetric(horizontal=8, vertical=4),
                    border=ft.Border.all(1, AMBER),
                ),
            ], spacing=12, vertical_alignment=ft.CrossAxisAlignment.CENTER),
            ft.Container(height=10),
            video_widget,
        ], spacing=0)
    else:
        video_content = ft.Column([
            ft.Icon(ft.Icons.VIDEO_CALL, color=BLUE, size=42),
            ft.Text("Safe Sphere — Semester Contribution Video", size=14,
                    weight=ft.FontWeight.BOLD, color=WHITE,
                    text_align=ft.TextAlign.CENTER),
            ft.Text("Put video.mp4 in the same folder as main2.py",
                    size=11, color=MUTED, text_align=ft.TextAlign.CENTER),
            ft.Container(
                ft.Text("1 minute 30 seconds maximum", size=10, color=AMBER,
                        weight=ft.FontWeight.BOLD),
                bgcolor=AMBER_DIM, border_radius=6,
                padding=ft.Padding.symmetric(horizontal=10, vertical=4),
                border=ft.Border.all(1, AMBER),
            ),
        ], spacing=8, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    video_section = ft.Container(
        content=video_content,
        bgcolor=CARD, border_radius=16, padding=16,
        border=ft.Border.all(1, BLUE+"40"),
        shadow=ft.BoxShadow(blur_radius=20, color=BLUE+"18", offset=ft.Offset(0, 4)),
    )

    cards = []
    for p in BLOG_POST:
        cards.append(ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Container(width=3, height=40, bgcolor=p["color"], border_radius=2),
                    ft.Column([
                        ft.Text(p["label"], size=9, color=p["color"],
                                weight=ft.FontWeight.BOLD,
                                style=ft.TextStyle(letter_spacing=1.5)),
                        ft.Text(p["title"], size=14, weight=ft.FontWeight.BOLD,
                                color=WHITE),
                    ], spacing=2, expand=True),
                ], spacing=12, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                ft.Container(height=8),
                ft.Text(p["body"], size=13, color=MUTED2, selectable=True),
            ], spacing=4),
            bgcolor=CARD, border_radius=14, padding=18,
            border=ft.Border.only(left=ft.BorderSide(3, p["color"])),
            shadow=ft.BoxShadow(blur_radius=12, color=p["color"]+"18",
                                offset=ft.Offset(0,3)),
        ))

    return ft.Column([
        ft.Container(
            content=ft.Row([
                page_title("Technical Blog", "What I learned building this app"),
                tag("LEARNING JOURNAL"),
            ], vertical_alignment=ft.CrossAxisAlignment.START),
            bgcolor=CARD, border_radius=16, padding=20,
            border=ft.Border.all(1, BORDER_C),
            shadow=ft.BoxShadow(blur_radius=20, color=BLUE+"18", offset=ft.Offset(0,4)),
        ),
        ft.Container(height=16),
        section_title("My 1-minute explanation video"),
        ft.Container(height=8),
        video_section,
        ft.Container(height=16),
        section_title("What I learned this semester"),
        ft.Container(height=8),
        *cards,
        ft.Container(height=20),
    ], spacing=12, scroll=ft.ScrollMode.AUTO, expand=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 4 — MATLAB HUB
# ══════════════════════════════════════════════════════════════════════════════
def matlab_view():
    image_display = ft.Container(
        content=ft.Column([
            ft.Icon(ft.Icons.TOUCH_APP, color=MUTED, size=36),
            ft.Text("Click any certificate to view it",
                    size=13, color=MUTED, text_align=ft.TextAlign.CENTER),
        ], spacing=8, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        bgcolor=CARD2, border_radius=14,
        border=ft.Border.all(1, BORDER_C),
        padding=40, alignment=ft.Alignment(0,0), height=280,
    )

    def make_tile(course):
        colors = [BLUE, TEAL, PURPLE, AMBER, GREEN, ROSE, BLUE, TEAL]
        idx = COURSES.index(course)
        c = colors[idx % len(colors)]

        def on_click(_):
            img_src = CERT_IMAGES.get(course["key"], "")
            image_display.content = ft.Column([
                ft.Text(course["name"], size=14, weight=ft.FontWeight.BOLD,
                        color=WHITE, text_align=ft.TextAlign.CENTER),
                ft.Text("Completed: " + course["date"], size=11,
                        color=c, text_align=ft.TextAlign.CENTER),
                ft.Image(src=img_src, width=500, fit="contain"),
            ], spacing=8, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            image_display.height = None
            image_display.update()

        return ft.Container(
            content=ft.Row([
                ft.Container(ft.Icon(ft.Icons.VERIFIED, color=BG, size=14),
                             width=28, height=28, bgcolor=c, border_radius=14,
                             alignment=ft.Alignment(0,0)),
                ft.Column([
                    ft.Text(course["name"], size=12,
                            weight=ft.FontWeight.BOLD, color=WHITE),
                    ft.Text(course["date"], size=10, color=c),
                ], spacing=2, expand=True),
                ft.Icon(ft.Icons.CHEVRON_RIGHT, color=MUTED, size=16),
            ], spacing=10, vertical_alignment=ft.CrossAxisAlignment.CENTER),
            bgcolor=CARD, border=ft.Border.all(1, BORDER_C),
            border_radius=10,
            padding=ft.Padding.symmetric(horizontal=14, vertical=10),
            on_click=on_click, ink=True, expand=True,
        )

    tiles = [make_tile(c) for c in COURSES]
    grid_rows = []
    for i in range(0, len(tiles), 2):
        pair = tiles[i:i+2]
        if len(pair) == 2:
            grid_rows.append(ft.Row(pair, spacing=10, expand=True))
        else:
            grid_rows.append(ft.Row([pair[0], ft.Container(expand=True)],
                                    spacing=10, expand=True))

    return ft.Column([
        ft.Container(
            content=ft.Row([
                page_title("MATLAB Hub", "MathWorks Learning Center"),
                tag("8 CERTIFICATES", AMBER, AMBER_DIM),
            ], vertical_alignment=ft.CrossAxisAlignment.START),
            bgcolor=CARD, border_radius=16, padding=20,
            border=ft.Border.all(1, BORDER_C),
            shadow=ft.BoxShadow(blur_radius=20, color=AMBER+"18", offset=ft.Offset(0,4)),
        ),
        ft.Container(height=12),
        glass_card(ft.Row([
            ft.Icon(ft.Icons.EMOJI_EVENTS, color=AMBER, size=24),
            ft.Column([
                ft.Text("8 of 8 courses completed", size=14,
                        weight=ft.FontWeight.BOLD, color=WHITE),
                ft.ProgressBar(value=1.0, bgcolor=BORDER_C, color=AMBER,
                               height=6, border_radius=ft.BorderRadius.only(
                                   top_left=3,top_right=3,bottom_left=3,bottom_right=3)),
            ], spacing=6, expand=True),
            ft.Container(
                ft.Text("100%", size=14, color=AMBER, weight=ft.FontWeight.BOLD),
                bgcolor=AMBER_DIM, border_radius=8,
                padding=ft.Padding.symmetric(horizontal=10, vertical=4),
                border=ft.Border.all(1, AMBER),
            ),
        ], spacing=14, vertical_alignment=ft.CrossAxisAlignment.CENTER),
        glow=AMBER),
        ft.Container(height=12),
        section_title("Click a certificate to view"),
        ft.Container(height=8),
        image_display,
        ft.Container(height=12),
        section_title("All 8 completed courses"),
        ft.Container(height=8),
        ft.Column(grid_rows, spacing=10),
        ft.Container(height=20),
    ], spacing=8, scroll=ft.ScrollMode.AUTO, expand=True)

# ══════════════════════════════════════════════════════════════════════════════
# TOP NAV + SHELL  (no sidebar — top navigation bar instead)
# ══════════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 5 — REFLECTION
# ══════════════════════════════════════════════════════════════════════════════
def reflection_view():
    # Logo loader
    def load_img(filename):
        import os, base64
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        try:
            with open(path, "rb") as f:
                return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()
        except Exception:
            return ""

    logo_src = load_img("logo.jpg")

    contrib_items = [
        "Contributing to the Software Requirements Specification (SRS).",
        "Documenting the project scope and problem statement.",
        "Defining functional and non-functional requirements.",
        "Assisting with use case documentation.",
        "Reviewing documentation for consistency and accuracy.",
        "Compiling final project documentation for submission.",
    ]

    doc_updates = [
        ("Documentation Update 1", ["Prepared and refined the SRS document.", "Reviewed project objectives and requirements."]),
        ("Documentation Update 2", ["Updated functional requirement descriptions.", "Verified consistency with planned application features."]),
        ("Documentation Update 3", ["Assisted in documenting use cases and user interactions.", "Improved clarity of system descriptions."]),
        ("Documentation Update 4", ["Conducted final proofreading and quality assurance checks before submission."]),
    ]

    learned_items = [
        "Software development lifecycle principles.",
        "Requirements gathering and analysis.",
        "Technical documentation techniques.",
        "Team collaboration and communication.",
        "Mobile application architecture.",
        "Database concepts and cloud technologies.",
        "User interface branding and design principles.",
        "The importance of safety systems in engineering environments.",
    ]

    def bullet_list(items, color=None):
        return ft.Column([
            ft.Row([
                ft.Container(width=6, height=6, bgcolor=color or BLUE,
                             border_radius=3),
                ft.Text(item, size=13, color=MUTED2, expand=True),
            ], spacing=10, vertical_alignment=ft.CrossAxisAlignment.START)
            for item in items
        ], spacing=8)

    def section_card(title, icon, icon_color, icon_bg, content):
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Container(ft.Icon(icon, color=icon_color, size=20),
                                 width=42, height=42, bgcolor=icon_bg,
                                 border_radius=12, alignment=ft.Alignment(0, 0)),
                    ft.Text(title, size=15, weight=ft.FontWeight.BOLD,
                            color=WHITE, expand=True),
                ], spacing=12, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                ft.Container(height=10),
                content,
            ], spacing=0),
            bgcolor=CARD, border=ft.Border.all(1, BORDER_C),
            border_radius=14, padding=20,
            shadow=ft.BoxShadow(blur_radius=12, color=BLUE+"18", offset=ft.Offset(0, 3)),
        )

    # Doc update cards
    update_cards = []
    for title, points in doc_updates:
        update_cards.append(ft.Container(
            content=ft.Column([
                ft.Text(title, size=12, weight=ft.FontWeight.BOLD, color=BLUE),
                *[ft.Row([
                    ft.Container(width=5, height=5, bgcolor=BLUE, border_radius=3),
                    ft.Text(p, size=12, color=MUTED2, expand=True),
                ], spacing=8) for p in points],
            ], spacing=6),
            bgcolor=BLUE_DIM, border_radius=10,
            padding=ft.Padding.symmetric(horizontal=14, vertical=12),
            border=ft.Border.only(left=ft.BorderSide(3, BLUE)),
        ))

    # Logo section
    logo_section = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Container(ft.Icon(ft.Icons.SHIELD, color=AMBER, size=20),
                             width=42, height=42, bgcolor=AMBER_DIM,
                             border_radius=12, alignment=ft.Alignment(0, 0)),
                ft.Text("Branding Contribution — Safe Sphere Logo", size=15,
                        weight=ft.FontWeight.BOLD, color=WHITE, expand=True),
            ], spacing=12),
            ft.Container(height=10),
            ft.Text("Designed the Safe Sphere application logo. The logo was created to "
                    "represent safety, protection, and hazard prevention through the use "
                    "of a shield-based concept. This contribution helped establish a "
                    "professional visual identity for the application and reinforced its "
                    "mission of promoting safety awareness in mining and industrial environments.",
                    size=13, color=MUTED2, selectable=True),
            ft.Container(height=14),
            ft.Container(height=14),
            ft.Column([
                ft.Row([
                    ft.Container(width=5, height=5, bgcolor=AMBER, border_radius=3),
                    ft.Text(p, size=12, color=MUTED2, expand=True),
                ], spacing=8)
                for p in [
                    "Designed the Safe Sphere logo.",
                    "Refined logo concepts based on project goals and team feedback.",
                    "Contributed to establishing the visual identity of the application.",
                ]
            ], spacing=8),
            ft.Container(height=16),
            ft.Container(
                content=ft.Image(src=logo_src, width=280, height=280, fit="contain")
                if logo_src else
                ft.Column([
                    ft.Icon(ft.Icons.IMAGE, color=MUTED, size=48),
                    ft.Text("Put logo.jpg in the same folder as main2.py",
                            size=12, color=MUTED,
                            text_align=ft.TextAlign.CENTER),
                ], spacing=6, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                bgcolor=CARD2, border_radius=14,
                alignment=ft.Alignment(0, 0),
                border=ft.Border.all(1, BORDER_C),
                padding=20,
                expand=True,
            ),
        ], spacing=0),
        bgcolor=CARD, border=ft.Border.all(1, BORDER_C),
        border_radius=14, padding=20,
        shadow=ft.BoxShadow(blur_radius=12, color=AMBER+"18", offset=ft.Offset(0, 3)),
    )

    return ft.Column([
        ft.Container(
            content=ft.Row([
                page_title("Reflection", "Individual contributions and learning"),
                tag("PORTFOLIO", PURPLE, PURPLE_DIM),
            ], vertical_alignment=ft.CrossAxisAlignment.START),
            bgcolor=CARD, border_radius=16, padding=20,
            border=ft.Border.all(1, BORDER_C),
            shadow=ft.BoxShadow(blur_radius=20, color=BLUE+"18", offset=ft.Offset(0, 4)),
        ),
        ft.Container(height=14),
        section_title("My Individual Contributions"),
        ft.Container(height=8),
        section_card(
            "Documentation Lead Responsibilities",
            ft.Icons.DESCRIPTION, BLUE, BLUE_DIM,
            ft.Column([
                ft.Text("My contributions to the project were focused on both documentation "
                        "and branding. As Documentation Lead, I worked closely with other team "
                        "members to gather system information and convert technical ideas into "
                        "clear and structured documentation.",
                        size=13, color=MUTED2, selectable=True),
                ft.Container(height=10),
                bullet_list(contrib_items, BLUE),
            ], spacing=0),
        ),
        ft.Container(height=12),
        section_title("Documentation Contribution Log"),
        ft.Container(height=8),
        ft.Container(
            content=ft.Column(update_cards, spacing=10),
            bgcolor=CARD, border_radius=14, padding=20,
            border=ft.Border.all(1, BORDER_C),
            shadow=ft.BoxShadow(blur_radius=12, color=BLUE+"18", offset=ft.Offset(0, 3)),
        ),
        ft.Container(height=12),
        section_title("Branding Contribution"),
        ft.Container(height=8),
        logo_section,
        ft.Container(height=12),
        section_title("What I Learned Throughout the Semester"),
        ft.Container(height=8),
        section_card(
            "Skills and Knowledge Gained",
            ft.Icons.LIGHTBULB, PURPLE, PURPLE_DIM,
            ft.Column([
                ft.Text("Throughout this project, I learned:",
                        size=13, color=MUTED2),
                ft.Container(height=8),
                bullet_list(learned_items, PURPLE),
                ft.Container(height=8),
                ft.Text("The project improved both my technical and professional skills.",
                        size=13, color=MUTED2),
            ], spacing=0),
        ),
        ft.Container(height=20),
    ], spacing=10, scroll=ft.ScrollMode.AUTO, expand=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 6 — CHALLENGES
# ══════════════════════════════════════════════════════════════════════════════
CHALLENGES = [
    {
        "num": "01", "color": "#EF4444", "bg": CARD2,
        "title": "Gathering Accurate Requirements",
        "challenge": "Different team members had different ideas regarding system features, making it difficult to produce a consistent and agreed-upon set of requirements.",
        "solution": "Regular discussions and document reviews were conducted to ensure that all requirements were accurately captured and agreed upon by all team members.",
    },
    {
        "num": "02", "color": AMBER, "bg": CARD2,
        "title": "Maintaining Documentation Consistency",
        "challenge": "As the project evolved, requirements changed and documentation needed frequent updates. Keeping all sections consistent with the latest project developments was time-consuming.",
        "solution": "Version control and regular reviews were used to keep documentation consistent with the latest project developments throughout the semester.",
    },
    {
        "num": "03", "color": PURPLE, "bg": CARD2,
        "title": "Designing a Meaningful Logo",
        "challenge": "Creating a logo that effectively represented safety while remaining visually appealing was challenging. The logo needed to communicate protection and hazard prevention clearly.",
        "solution": "Safety-related symbols were researched and a shield-based design was selected that clearly communicates protection, security, and hazard prevention while maintaining a professional appearance.",
    },
]

def challenges_view():
    cards = []
    for ch in CHALLENGES:
        cards.append(ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Container(
                        ft.Text(ch["num"], size=20, weight=ft.FontWeight.BOLD,
                                color=ch["color"]),
                        width=50, height=50, bgcolor=ch["bg"],
                        border_radius=14, alignment=ft.Alignment(0, 0),
                        border=ft.Border.all(1, ch["color"] + "50"),
                    ),
                    ft.Text(ch["title"], size=15, weight=ft.FontWeight.BOLD,
                            color=WHITE, expand=True),
                ], spacing=14, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                ft.Container(height=12),
                ft.Container(
                    content=ft.Column([
                        ft.Text("CHALLENGE", size=9, color="#EF4444",
                                weight=ft.FontWeight.BOLD,
                                style=ft.TextStyle(letter_spacing=1.5)),
                        ft.Container(height=4),
                        ft.Text(ch["challenge"], size=12, color=MUTED2, selectable=True),
                    ], spacing=0),
                    bgcolor=CARD2, border_radius=8,
                    padding=ft.Padding.symmetric(horizontal=14, vertical=12),
                    border=ft.Border.only(left=ft.BorderSide(3, "#EF4444")),
                ),
                ft.Container(height=8),
                ft.Container(
                    content=ft.Column([
                        ft.Text("HOW I ADDRESSED IT", size=9, color=GREEN,
                                weight=ft.FontWeight.BOLD,
                                style=ft.TextStyle(letter_spacing=1.5)),
                        ft.Container(height=4),
                        ft.Text(ch["solution"], size=12, color=MUTED2, selectable=True),
                    ], spacing=0),
                    bgcolor=CARD2, border_radius=8,
                    padding=ft.Padding.symmetric(horizontal=14, vertical=12),
                    border=ft.Border.only(left=ft.BorderSide(3, GREEN)),
                ),
            ], spacing=0),
            bgcolor=CARD, border=ft.Border.all(1, BORDER_C),
            border_radius=14, padding=20,
            shadow=ft.BoxShadow(blur_radius=12, color=BLUE+"18", offset=ft.Offset(0, 3)),
        ))

    return ft.Column([
        ft.Container(
            content=ft.Row([
                page_title("Challenges", "Problems encountered and solutions"),
                tag("3 CHALLENGES", ROSE, ROSE_DIM),
            ], vertical_alignment=ft.CrossAxisAlignment.START),
            bgcolor=CARD, border_radius=16, padding=20,
            border=ft.Border.all(1, BORDER_C),
            shadow=ft.BoxShadow(blur_radius=20, color=BLUE+"18", offset=ft.Offset(0, 4)),
        ),
        ft.Container(height=14),
        section_title("Challenges encountered and how I addressed them"),
        ft.Container(height=8),
        *cards,
        ft.Container(height=20),
    ], spacing=14, scroll=ft.ScrollMode.AUTO, expand=True)

NAV_ITEMS = [
    ("Timeline",   ft.Icons.CALENDAR_VIEW_WEEK, "timeline"),
    ("GitHub",     ft.Icons.CODE,               "github"),
    ("Blog",       ft.Icons.EDIT_NOTE,          "blog"),
    ("MATLAB",     ft.Icons.SCHOOL,             "matlab"),
    ("Reflection", ft.Icons.AUTO_STORIES,       "reflection"),
    ("Challenges", ft.Icons.ENGINEERING,        "challenges"),
]
VIEW_MAP = {
    "timeline":   timeline_view,
    "github":     github_view,
    "blog":       blog_view,
    "matlab":     matlab_view,
    "reflection": reflection_view,
    "challenges": challenges_view,
}

def build_topbar(page, active):
    def make_btn(label, icon, key):
        is_active = key == active
        def on_click(_):
            page.data["active"] = key
            rebuild(page)
        return ft.Container(
            content=ft.Row([
                ft.Icon(icon,
                        color=BLUE if is_active else MUTED,
                        size=16),
                ft.Text(label,
                        color=WHITE if is_active else MUTED,
                        size=13,
                        weight=ft.FontWeight.BOLD if is_active else ft.FontWeight.NORMAL),
            ], spacing=8),
            padding=ft.Padding.symmetric(horizontal=16, vertical=10),
            border=ft.Border.only(bottom=ft.BorderSide(2, BLUE if is_active else "transparent")),
            on_click=on_click, ink=True,
        )

    # Avatar
    avatar = ft.Container(
        content=(
            ft.Container(
                ft.Image(src=PROFILE_PHOTO_SRC, width=36, height=36, fit="cover"),
                width=36, height=36, border_radius=18,
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            ) if PROFILE_PHOTO_SRC and len(PROFILE_PHOTO_SRC) > 10 else
            ft.Text(STUDENT_INITIALS, color=WHITE, size=14,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER)
        ),
        width=36, height=36, bgcolor=BLUE_DIM, border_radius=18,
        alignment=ft.Alignment(0,0),
        border=ft.Border.all(2, BLUE),
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
    )

    return ft.Container(
        content=ft.Row([
            # Brand
            ft.Row([
                ft.Container(
                    ft.Text("G3", color="#FFFFFF", size=13, weight=ft.FontWeight.BOLD),
                    bgcolor=BLUE, border_radius=8, width=32, height=32,
                    alignment=ft.Alignment(0,0),
                ),
                ft.Column([
                    ft.Text(STUDENT_NAME, color=WHITE, size=13,
                            weight=ft.FontWeight.BOLD),
                    ft.Text("Documentation Lead | Group 3",
                            color=MUTED, size=10),
                ], spacing=0),
            ], spacing=10),
            ft.Container(expand=True),
            # Nav buttons
            ft.Row([make_btn(l, i, k) for l, i, k in NAV_ITEMS], spacing=0),
            ft.Container(expand=True),
            # Avatar
            avatar,
        ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
        bgcolor=NAV_BG,
        padding=ft.Padding.symmetric(horizontal=24, vertical=0),
        height=56,
        border=ft.Border.only(bottom=ft.BorderSide(1, BORDER_C)),
        shadow=ft.BoxShadow(blur_radius=8, color='#1A6366F1', offset=ft.Offset(0,2)),
    )

def rebuild(page):
    active = page.data.get("active", "timeline")
    content = VIEW_MAP[active]()
    topbar  = build_topbar(page, active)
    page.controls.clear()
    page.controls.append(ft.Column([
        topbar,
        ft.Container(
            content=content,
            expand=True,
            bgcolor=BG,
            padding=ft.Padding.only(left=36, right=36, top=24, bottom=0),
        ),
    ], spacing=0, expand=True))
    page.update()

def main(page: ft.Page):
    page.title         = f"{STUDENT_NAME} — Portfolio"
    page.theme_mode    = ft.ThemeMode.LIGHT
    page.bgcolor       = BG
    page.padding       = 0
    page.window.width  = 1150
    page.window.height = 780
    page.data          = {"active": "timeline"}
    rebuild(page)

ft.run(main, assets_dir="assets")