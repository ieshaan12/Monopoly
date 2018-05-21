class player
    {char name[30];
     float money;
     public:
     player()
        {cout<<"Player Created"<<endl;
        }
    };
class property
    {char name[30];
     float price;
     float rent;
     float costoc;
     float costoh;
     float rentpc;
     float rentph;
     int noc;
     int noh;
// ADD OWNERSHIP DETAILS, SET TO BANK IF NO OWNER. See inheritance, or create player object.
    public:
    void prompt()
    {cout<<"Property Details as follows"<<endl;
    cout<<"Price :"<<price<<endl;
    cout<<"Rent :"<<rent<<endl;
    cout<<"Cost Of Cottage :"<<costoc<<"\tCost of Hotel :"<<costoh<<endl;
    cout<<"Rent per Cottage :"<<rentpc<<"\tRent per Hotel: "<<rentph<<endl;
    }
        };
