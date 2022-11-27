# Membuat Dictionary
saya = {
    "nama": "M. Ghozi Syah Putra",
    "umur": 18,
    "hobi": ["coding", "nonton anime", "game"],
    "menikah": False,
    "sosmed": {
        "instagram": "@mghozi__",
        "github": "Shadow-Killer"
    }
}
# Mengakses isi dictionary
print("Nama saya adalah %s" % saya["nama"])
print("Hobi : %s" % saya["hobi"])
print("Github: %s" % saya["sosmed"]["github"])