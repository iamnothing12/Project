#BASIC HTML
DOCUMENT_TPYE = '<!DOCTYPE>' # Defines the document type
HTML = 'html' # Defines an HTML document
HEAD = 'head' # Defines information about the document
TITLE = 'title' # Defines a title for the document
BODY = 'body' # Defines the document's body
HEAD1 = 'h1' # Define HTML Headings
HEAD2 = 'h2' # Define HTML Headings
HEAD3 = 'h3' # Define HTML Headings
HEAD4 = 'h4' # Define HTML Headings
HEAD5 = 'h5' # Define HTML Headings
HEAD6 = 'h6' # Define HTML Headings
PARAGRAPH = 'p' # Defines a paragraph
BR = 'br' # Insert a single line break
HR = 'hr' # Defines a thematic change in the content
START_COMMENT = '<!--' # Defines a comment start
END_COMMENT = '-->' # Defines a comment end

#Formatting
ABBREVIATION = 'abbr' # Defines an abbreviation or an acronym
ADDRESS = 'address' # Defines contact information for the author/owner of a document/article
BOLD = 'b' # Bold text
ISOLATE_TEXT = 'bdi' # Isolates a part of text that might be formatted in a differnt direction from the other text outside it
OVERRIDE_TEXT_DIRECTION = 'bdo' # Overrides the current text direction
BLOCKQUOTE = 'blockquote' # Defines a section that is quoted from another source
CITE = 'cite' # Defines the title of a work
CODE = 'code' # Defines a piece of computer code
DELETE = 'del' # Defines text that has been deleted from a document
DEFINE_INSTANCE = 'dfn' # Represents the defining instance of a term
EMPHASIZED_TEXT = 'em' # Define Emphasize text
ALTERNATE_TEXT = 'i' # Define a part of text in an alternate voice or mood
INSERT_TEXT = 'ins' # Define a text that has been inserted into a document
KEYBOARD_INPUT = 'kbd' #Define a keyboard input
MARK_TEXT = 'mark' # Define marked/highlighted text
METER = 'meter' # Define a scalar measurement within a known range 
PRE = 'pre' # Define preformmatted text
PROGRESS = 'progress' # Represent the progress of a task
QUOTE = 'q' # Defines a short quotation
RUBY_ANNOTATION = 'rp' # Defines what to show in browser that do not support ruby annotations
EAST_ASIAN_TYPOGRAPHY = 'rt' # Define an explanation/pronunciation of characters
RUBY = 'ruby' # Define a ruby annotation
WRONG_TEXT = 's' # Define text is no longer correct
SAMPLE_OUTPUT = 'samp' # Defines sample output from a computer program
SMALL = 'small' # Defines smaller text
STRONG = 'strong' # Defines important text
SUB = 'sub' # Defines subscripted text
SUP = 'sup' # Defines superscripted text
TEMPLATE = 'template' # Defines a template
TIME = 'time' # Defines a date/time
STYLE_TEXT = 'u' # Define text that should be stylistically different form normal text
VARIABLE = 'var' # Defines a variable
POSSIBLE_LINE_BREAK = 'wbr' #Defines possible line-break

#Form and Input
FORM = 'form' # Defines an HTML form for user input
INPUT = 'input' # Defines an input control
TEXTAREA = 'textarea' # Defines a multiline input control (text area)
BUTTON = 'button' # Defines a clickable button
SELECT = 'select' # Defines a drop-down list
OPTGROUP = 'optgroup' # Defines a group of related options in a drop-down list
OPTION = 'option' # Defines an option in a drop-down list
LABEL = 'label' # Defines a label for an <input> element
FIELDSET = 'fieldset' #	Groups related elements in a form
LEGEND = 'legend' # Defines a caption for a <fieldset> element
DATALIST = 'datalist' # Specifies a list of pre-defined options for input controls
OUTPUT = 'output' # Defines the result of a calculation

#Frames
IFRAME = 'iframe' # Define an inline frame

#Images
IMG = 'img' # Defines an image
MAP = 'map' # Defines a client-side image-map
AREA = 'area' # Defines an area inside an image-map
CANVAS = 'canvas' # Used to draw graphics, on the fly, via scripting
FIG_CAPTION = 'figcaption' # Defines a caption for a <figure> element
FIGURE = 'figure' # Specifies self-contained content
PICTURE = 'picture' # Defines a container for multiple image resources
SVG = 'svg' # Defines a container for SVG graphics

#Audio/Video
AUDIO = 'audio' # Defines sound content
SOURCE = 's5ource' # Defines multiple media resources for media elements(<video>, <audio> and <picture>)
TRACK = 'track' # Defines text tracks for media elements (<video> and <audio>)
VIDEO = 'video' # Defines a video or movie

#Links
HYPERLINK_A = 'a' # Defines a hyperlink
LINK = 'link' # Defines the relationship between a document and an external resource (most used to link to style sheets)
NAVIGATION = 'nav' # Defines navigation links

#List
UNORDER_LIST = 'ul' # Defines an unordered list
ORDERED_LIST = 'ol' # Defines an ordered list
LIST_ITEM = 'li' # Defines a list item
DESCRIPTION_LIST = 'dl' # Defines a description list
DESCRIPTION_LIST_TERM = 'dt' # Defines a term/name in a description list
DESCRIPTION_LIST_TERM_TERM = 'dd' # Defines a description of a term/name in a description list

#Tables
TABLES = 'table' # Defines a table
CAPTION = 'caption' # Defines a table caption
TABLE_HEADER = 'th' # Defines a header cell in a table
TABLE_ROW = 'tr' # Defines a row in a table
TABLE_CELL = 'td' # Defines a cell in a table
GROUP_TABLE_HEADER = 'thead' # Groups the header content in a table
GROUP_TABLE_BODY = 'tbody' # Groups the body content in a table
GROUP_TABLE_FOOTER = 'tfoot' # Groups the footer content in a table
COLUMN_PROPERTIES = 'col' # Specifies column properties for each column within a <colgroup> element
COLUMN_GROUP = 'colgroup' # Specifies a group of one or more columns in a table for formatting

#Style and Semantics
STYLE = 'style' # Defines style information for a document
DIV = 'div' # Defines a section in a document
SPAN = 'span' # Defines a section in a document
HEADER = 'header' # Defines a header for a document or section
FOOTER = 'footer' # Defines a footer for a document or section
MAIN = 'main' # Specifies the main content of a document
SECTION = 'section' # Defines a section in a document
ARTICLE = 'article' # Defines an article
ASIDE = 'aside' # Defines content aside from the page content
DETAILS = 'details' # Defines additional details that the user can view or hide
DIALOG = 'dialog' # Defines a dialog box or window
SUMMARY = 'summary' # Defines a visible heading for a <details> element
DATA = 'data' # Links the given content with a machine-readable translation

#Meta Info
# HEAD = 'head' #Defines information about the document
META = 'meta' # Defines metadata about an HTML document
BASE = 'base' # Specifies the base URL/target for all relative URLs in a document

#Programming
SCRIPT = 'script' # Defines a client-side script
NO_SCRIPT = 'noscript' # Defines an alternate content for users that do not support client-side scripts
EMBED = 'embed' # Defines a container for an external (non-HTML) application
OBJECT = 'object' # Defines an embedded object
PARAM = 'param' # Defines a parameter for an object