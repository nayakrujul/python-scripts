from requests import get


print(
    "Supported languages:",
    "English = 'en'",
    "German = 'de'",
    "Spanish = 'es'",
    "Dutch = 'nl'",
    "Polish = 'pl'",
    "Italian = 'it'",
    "Czech = 'cz'",
    "Translation to or from German.",
    "",
    sep="\n"
)

q = input("Word to be translated: ")
lang = input("From: ").lower() + "-" + input("To: ").lower()

if lang not in (
                'de-en',
                'de-es',
                'de-nl',
                'de-pl',
                'de-it',
                'de-cs',
                'en-de',
                'es-de',
                'nl-de',
                'pl-de',
                'it-de',
                'cs-de'
        ):
    lang = 'en-de'

print("Connecting...\n")

response = get(
    'https://lt-translate-test.herokuapp.com/'
    f'?langpair={lang}'
    f'&query={q}'
).json()

if len(response):

    data = response[0]

    print("Best translation -", data['l1_text'], "=", data['l2_text'])
    print("Synonyms:")
    for i in range(len(data['synonyme1'].split(", "))):
        try:
            print((20 - len(data['synonyme1'].split(", ")[i])) * " ", data['synonyme1'].split(", ")[i], "|", data['synonyme2'].split(", ")[i])
        except:
            break
    print("Frequency -", data['freq'])

else:

    print("Not found.")

print("\nAPI:\nhttps://lt-translate-test.herokuapp.com/\nhttps://linguatools.org/")
