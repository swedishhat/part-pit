package component

type Component struct {
	ID            string
	Name          string
	Description   string
	Category      string
	Lifecycle     string
	ExternalLinks []ExternalLink
}

type ExternalLink struct {
	Name     string
	LinkType string
	URI      string
}

type Resistor struct {
	Parameter
}

func New(ID string, Name string, Description string, Category string, Lifecycle string, ExternalLinks []ExternalLink, Parameters []Parameter) Resistor {
}
