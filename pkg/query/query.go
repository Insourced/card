package query

type m_magic_card struct {
	name   string
	kind   string
	mana   int
	number int
	effect string
}

type m_creature_card struct {
	name    string
	health  int
	mana    int
	number  int
	attacks [4]attack
}

type attack struct {
	name string
	dmg  int
	mana int
}

func Parse(kind string) {
	if kind == "magic" {
		m_query_magic()
	}
	if kind == "creature" {
		m_query_creature()
	} else {
		panic("you either can't spell or do not know how to use this.")
	}
}

func m_query_magic()    {}
func m_query_creature() {}
