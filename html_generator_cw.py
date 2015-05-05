#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cw8627
#
# Created:     22/04/2015
# Copyright:   (c) cw8627 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def generate_concept_HTML(concept, concept_brief, concept_description):
    html_text_1 = '''
<div class="concept">
      ''' + concept
    html_text_2 = '''
    </div>

    <div class="concept-brief">
        ''' + concept_brief
    html_text_3 = '''
    </div>

<div class="concept-description">
      ''' + concept_description
    html_text_4 = '''
</div>'''

    full_html_text = html_text_1 + html_text_2 + html_text_3 + html_text_4
    return full_html_text

def make_HTML(concept_list):
    concept = concept_list[0]
    concept_brief = concept_list[1]
    concept_description = concept_list [2]
    return generate_concept_HTML(concept, concept_brief, concept_description)

EXAMPLE_LIST_OF_CONCEPTS = [ ['Structured Data', 'Lists and strings',
                              'Strings and lists are both types of structured data.'],
                             ['Mutation', 'Alien DNA',
                             'Mutations are supported by lists but not strings.'],
                             ['Aliasing', 'A Rose by any other name',
                               'Aliasing is two different ways to refer to the same object'] ]


def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)
