from django import forms
from .models import DmatsAccount, Share
from django.contrib.auth.models import User



class DmatsForm(forms.ModelForm):
    class Meta:
        model = DmatsAccount
        fields = ('name','capital','username','password','crn','pin')
        #select tag for capital field

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
        self.fields['name'].widget.attrs.update({'class': 'form-control',
        'placeholder':'Your Name',
        'type':'text',
        #form validation
        'required':'required',
        'pattern':'[a-zA-Z ]+',
        })

        CHOICES =[
            ("","Select Depository Participants"),
            ("13200","ABC SECURITIES PRIVATE LIMITED"),
("12300","AGRAWAL SECURITIES PRIVATE LIMITED"),
("17200","AGRICULTURAL DEVELOPMENT BANK LIMITED"),
("11900","ARYATARA INVESTMENT AND SECURITIES PRIVATE LIMITED"),
("15600","ASHUTOSH BROKERAGE AND SECURITIES PRIVATE LIMITED"),
("17500","ASIAN CAPITAL LIMITED"),
("14700","ASIAN SECURITIES PRIVATE LIMITED"),
("11100","BANK OF KATHMANDU LIMITED"),
("15000","BHRIKUTI STOCK BROKING COMPANY PRIVATE LIMITED"),
("16000","CENTURY COMMERCIAL BANK LIMITED"),
("11700","CITIZENS BANK INTERNATIONAL LIMITED"),
("10100","CIVIL CAPITAL MARKET LIMITED"),
("13300","CREATIVE SECURITIES PRIVATE LIMITED"),
("13400","CRYSTAL KANCHANJUNGHA SECURITIES PVT. LTD"),
("12000","DAKSHINKALI INVESTMENT AND SECURITIES PRIVATE LIMITED"),
("14500","DEEVYAA SECURITIES & STOCK HOUSE PRIVATE LIMITED"),
("11300","DIPSHIKHA DHITOPATRA KAROBAR COMPANY (P.) LTD."),
("14900","DYNAMIC MONEY MANAGERS SECURITIES PRIVATE LIMITED"),
("10800","EVEREST BANK LTD."),
("17600","GARIMA CAPITAL LIMITED"),
("12200","GLOBAL IME BANK LIMITED"),
("11200","GLOBAL IME CAPITAL LIMITED"),
("16200","GUHESWORI MERCHANT BANKING & FINANCE LIMITED"),
("18000","GURKHAS FINANCE LIMITED"),
("17700","HIMALAYAN CAPITAL LIMITED"),
("17400","ICFC FINANCE LIMITED"),
("13100","IMPERIAL SECURITIES COMPANY PRIVATE LIMITED"),
("17900","JYOTI BIKASH BANK LIMITED"),
("18700","KALIKA SECURITIES PVT. LTD."),
("18200","KAMANA SEWA BIKAS BANK LIMITED."),
("14300","KOHINOOR INVESTMENT & SECURITIES PRIVATE LIMITED"),
("15200","KUMARI BANK LIMITED"),
("10700","LAXMI CAPITAL MARKET LTD."),
("13800","LINCH STOCK MARKET LIMITED"),
("16100","MACHHAPUCHCHHRE BANK LIMITED"),
("14100","MACHHAPUCHCHHRE CAPITAL LIMITED"),
("16700","MAHALAXMI BIKAS BANK LIMITED"),
("17300","MEGA CAPITAL MARKETS LIMITED"),
("12500","MUKTINATH CAPITAL LIMITED"),
("15900","NAASA SECURITIES COMPANY LTD"),
("15100","NABIL BANK LIMITED"),
("16800","NABIL BANK LIMITED"),
("10400","NABIL INVESTMENT BANKING LTD."),
("15700","NEPAL BANK LIMITED"),
("16300","NEPAL CREDIT AND COMMERCE BANK LIMITED"),
("15500","NEPAL DP LIMITED"),
("15300","NEPAL SBI BANK LIMITED"),
("11500","NEPAL STOCK HOUSE PRIVATE LIMITED"),
("10200","NIBL ACE CAPITAL LIMITED"),
("10600","NIBL ACE CAPITAL LIMITED"),
("13700","NIC ASIA BANK LIMITED"),
("11000","NMB CAPITAL LIMITED"),
("11800","ONLINE SECURITIES PRIVATE LIMITED"),
("17000","OXFORD SECURITIES PVT. LTD."),
("13900","PRABHU BANK LIMITED"),
("12600","PRABHU CAPITAL LIMITED"),
("14800","PREMIER SECURITIES COMPANY LIMITED"),
("16900","PRIME COMMERCIAL BANK LIMITED"),
("15400","PRIME COMMERCIAL BANK LIMITED"),
("12800","PRIMO SECURITIES PRIVATE LIMITED"),
("18600","PROGRESSIVE FINANCE LIMITED"),
("16600","PROVIDENT MERCHANT BANKING LIMITED"),
("16500","RBB MERCHANT BANKING LIMITED"),
("18100","SAMPANNA CAPITAL AND ADVISORY NEPAL LIMITED"),
("14400","SANI SECURITIES COMPANY LIMITED"),
("15800","SANIMA BANK LTD"),
("11600","SECURED SECURITIES LIMITED"),
("12700","SEWA SECURITIES PRIVATE LIMITED"),
("18400","SHANGRI-LA DEVELOPMENT BANK LIMITED"),
("18500","SHINE RESUNGA DEVELOPMENT BANK LIMITED"),
("18800","SHREE INVESTMENT AND FINANCE CO. LTD."),
("12900","SHREE KRISHNA SECURITIES LIMITED"),
("10900","SIDDHARTHA CAPITAL LIMITED"),
("14600","SIPLA SECURITIES PRIVATE LIMITED"),
("13000","SOUTH ASIAN BULLS PRIVATE LIMITED"),
("14000","SRI HARI SECURITIES PVT. LTD."),
("14200","SUMERU SECURITIES PRIVATE LIMITED"),
("17800","SUNDHARA SECURITIES LIMITED"),
("12400","SUNRISE CAPITAL LIMITED"),
("18300","SWARNALAXMI SECURITIES PVT. LTD."),
("11400","TRISHAKTI SECURITIES PUBLIC LIMITED"),
("17100","TRISHUL SECURITIES & INVESTMENT LIMITED"),
("13500","VISION SECURITIES PVT. LTD")
    
        ]
        #select tag with search option
        

        self.fields['capital'].widget =(
          

            forms.Select(choices=CHOICES, attrs={'class': 'form-control',
                'data-live-search':'true',
                'data-filter':'true',
                'required':'true',
            })
        )

        self.fields['username'].widget.attrs.update({'class': 'form-control',
         'placeholder':'8-Digit Username',
         'type':'number',
         'required':'true',
         'pattern':'[0-9]{8}',


        })

        self.fields['password'].widget.attrs.update({'class': 'form-control',
        'placeholder':'Your Password',
        'type':'password',
        'required':'true',
        })
        self.fields['crn'].widget.attrs.update({'class': 'form-control',
        'placeholder':'CRN Number',
        'type':'text',
        'required':'true',
        'pattern':'[a-zA-Z0-9_-]*',
        })
        self.fields['pin'].widget.attrs.update({'class': 'form-control',
        'placeholder':'4-Digit PIN',
        'type':'number',
        'required':'true',
        'pattern':'[0-9]{4}',
        })




class ApplyShareForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = ('username','qty')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #show this form to only logged in users
        #change the label of the username field
        self.fields['username'].label = "Select Accounts"
        self.fields['username'].widget.attrs.update({'class': 'form-control',
        'type':'number'
        })

        self.fields['qty'].widget.attrs.update({'class': 'form-control',
        'type':'number'
        })

     


