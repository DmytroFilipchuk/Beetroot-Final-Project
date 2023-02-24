from state_tree.about_section.contact_info import Contact_info
from state_tree.about_section.our_playlist import MyPlaylist
from state_tree.about_section.website import Website
from state_tree.about_us import AboutUs
from state_tree.change_phone_number import Change_phone_number
from state_tree.ffeel_tools.converter import Converter
from state_tree.ffeel_tools.ffeeltools import FFeelTools
from state_tree.ffeel_tools.reference import Reference
from state_tree.main_menu import MainMenu
from state_tree.make_an_order.calendar import Create_calendar
from state_tree.make_an_order.client import Client
from state_tree.make_an_order.confirmed import Confirmed
from state_tree.make_an_order.ghostwriting_section import Ghostwriting
from state_tree.make_an_order.our_services import OurServices
from state_tree.make_an_order.question_list import Questions
from state_tree.make_an_order.recording_section import Recording
from state_tree.make_an_order.session_musician_section import SessionMusician
from state_tree.question_answers.five import Five
from state_tree.question_answers.four import Four
from state_tree.question_answers.one import One
from state_tree.question_answers.three import Three
from state_tree.question_answers.two import Two
from state_tree.settings import Settings

buttons_dict = {"phone_number" : Change_phone_number,
                "menu" : MainMenu,
                "client" : Client,
                "ffeeltools" : FFeelTools,
                "settings" : Settings,
                "about" : AboutUs,
                "contact" : Contact_info,
                "playlist_spotify" : MyPlaylist,
                "website" : Website,
                "recording" : Recording,
                "ghost_writer" : Ghostwriting,
                "session_musician" : SessionMusician,
                "services" : OurServices,
                "questions" : Questions,
                "reference" : Reference,
                "converter" : Converter,
                "one" : One,
                "two" : Two,
                "three" : Three,
                "four" : Four,
                "five" : Five,
                "calendar" : Create_calendar,
                "yes" : Confirmed,
                "no" : OurServices
                }