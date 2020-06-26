from ictk import igc


def test_rmh_parsing():
    result = igc.read_rmh_file("./tests/rmh_test_file.txt")
    # fmt: off
    assert result == (
        ("Fyrirlestraröð", "Framfara", "stendur", "fyrir", "fyrirlestri", "um", "ástæður", "ofþjálfunar", ",", "einkenni", "og", "meðferð", "."),
        ("Hættir", "fólki", "af", "ákveðinni", "persónugerð", "við", "ofþjálfun", "meira", "en", "öðrum", "?"),
        ("Hvaða", "áhrif", "hafa", "næring", ",", "svefn", "og", "hvíld", "?"),
        ("Stund", "og", "staður", ":"),
        ("Fimmtudaginn", "22.", "nóvember", "2012", "kl.", "19:30", "–", "21:00", "."),
        ("Íþróttamiðstöðin", "Laugardal", ",", "salur", "D."),
        ("Fyrirlesarar", ":"),
        ("Þórarinn", "Sveinsson", ",", "Dr.", "í", "lífeðlisfræði", ",", "dósent", "við", "HÍ"),
        ("Fríða", "Rún", "Þórðardóttir", ",", "MSc", "í", "næringarfræði", ",", "íþróttanæringarfræðingur"),
        ("Hafrún", "Kristjánsdóttir", ",", "Ma.", "í", "sálfræði", ",", "dósent", "við", "HR"),
        ("Aðgangseyrir", "er", "1000", "kr", "og", "rennur", "óskiptur", "til", "Framfara", ",", "hollvinafélags", "millivegalengda", "-", "og", "langhlaupara", "."),
    )
    # fmt: on
