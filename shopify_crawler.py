import requests
from tqdm import tqdm

def get_actual_domain(shopify_subdomain):
    try:
        # Build the Shopify URL
        url = f"https://{shopify_subdomain}"
        
        # Send a GET request and allow redirection
        response = requests.get(url, timeout=10, allow_redirects=True)
        
        # Extract the final redirected URL
        actual_domain = response.url
        
        # Return only the domain name
        return actual_domain.split("//")[-1].split("/")[0]
    except Exception as e:
        # Return an error message if something goes wrong
        return f"Error: {str(e)}"

def crawl_shopify_subdomains(subdomains):
    results = []
    for subdomain in tqdm(subdomains, desc="Crawling Shopify Subdomains"):
        actual_domain = get_actual_domain(subdomain)
        results.append((subdomain, actual_domain))
    return results

# List of Shopify subdomains
shopify_subdomains = [
"my-celebrity-closet.myshopify.com",
"vetchy.myshopify.com",
"alievastore.myshopify.com",
"skullshaver.myshopify.com",
"montaneuk.myshopify.com",
"chelsey-smith-cosmetics.myshopify.com",
"combat-iron-apparel.myshopify.com",
"smocked-auctions-development-site.myshopify.com",
"pacsafe-ltd.myshopify.com",
"aromatech-systems-canada.myshopify.com",
"til-valhalla-project.myshopify.com",
"bowmarnutrition.myshopify.com",
"shakawear-com.myshopify.com",
"cipo-and-baxx-t.myshopify.com",
"skullshaveruk.myshopify.com",
"chipre-basic-denim.myshopify.com",
"miik.myshopify.com",
"bellybandit.myshopify.com",
"ganactive-com.myshopify.com",
"acme-merino.myshopify.com",
"mamma-mia-covers.myshopify.com",
"theclothesrak.myshopify.com",
"michael-aram.myshopify.com",
"georgia-hardinge.myshopify.com",
"mycollegeshirt.myshopify.com",
"beyond-polish.myshopify.com",
"amalli-talli.myshopify.com",
"meindl-usa.myshopify.com",
"ink-alloy-2.myshopify.com",
"srchealth.myshopify.com",
"oneill-au.myshopify.com",
"thirtytwo-us.myshopify.com",
"dolly-l-llc.myshopify.com",
"famous-footwear-shop.myshopify.com",
"tungsten-fashion-jewelry.myshopify.com",
"the-perfect-arm.myshopify.com",
"loveandfit.myshopify.com",
"wearewhatwere.myshopify.com",
"thehisplacestore.myshopify.com",
"jackie-london.myshopify.com",
"good-feet-new-orleans.myshopify.com",
"les-coupons-de-saint-pierre.myshopify.com",
"etnies-us.myshopify.com",
"oak-pearl-clothingco.myshopify.com",
"mcs-apparel-shop.myshopify.com",
"flyingcolorsbaby.myshopify.com",
"ftficonversion.myshopify.com",
"muurswagg.myshopify.com",
"hansen-gretel-prod.myshopify.com",
"leona-test.myshopify.com",
"shopatshowcase.myshopify.com",
"rh-signature-co.myshopify.com",
"weekendbee.myshopify.com",
"shell-station.myshopify.com",
"the-gold-gods.myshopify.com",
"undgretel.myshopify.com",
"echelon-store.myshopify.com",
"uk-jewellery-king.myshopify.com",
"scrtco.myshopify.com",
"marco-calzature-milano.myshopify.com",
"kamoskinz.myshopify.com",
"simply-tall-inc.myshopify.com",
"theshoppemiami.myshopify.com",
"dermalogica-uk.myshopify.com",
"raishma-co-uk.myshopify.com",
"roosbeach.myshopify.com",
"twotags-au.myshopify.com",
"bevilles-jewellers.myshopify.com",
"lower-shop.myshopify.com",
"awake-mode.myshopify.com",
"paris-texas-apparel-co-2.myshopify.com",
"lug-nut-guys.myshopify.com",
"esskateboarding-us.myshopify.com",
"branded-uniform-solutions.myshopify.com",
"avenuemontaigne.myshopify.com",
"kiwi-diamond.myshopify.com",
"thehavenco.myshopify.com",
"cliquefitness.myshopify.com",
"aret-basewear.myshopify.com",
"lucieandleo.myshopify.com",
"cabourn.myshopify.com",
"grayling.myshopify.com",
"vaistoa.myshopify.com",
"blakshop.myshopify.com",
"shop-carine.myshopify.com",
"peau-de-loup.myshopify.com",
"golden-breed.myshopify.com",
"sportive-plus.myshopify.com",
"dermalogica-ca.myshopify.com",
"pompomme-shop.myshopify.com",
"claddaghringstore.myshopify.com",
"ownley-online.myshopify.com",
"emerica-us.myshopify.com",
"ooh-la-loft.myshopify.com",
"shop-zaikamoya.myshopify.com",
"isle-of-mine.myshopify.com",
"tileboom.myshopify.com",
"wolven-threads.myshopify.com",
"ltz-belts.myshopify.com",
"bluhq.myshopify.com",
"webx-6efb.myshopify.com",
"berry-jane-usa.myshopify.com",
"cognative-mtb.myshopify.com",
"ideaparktest.myshopify.com",
"pacsafe-eu.myshopify.com",
"bikinibible.myshopify.com",
"romika-usa.myshopify.com",
"shrimps-com.myshopify.com",
"assefs.myshopify.com",
"sigrcc.myshopify.com",
"luxe-tones.myshopify.com",
"emmydeveaux.myshopify.com",
"shop-freya.myshopify.com",
"premiata-us.myshopify.com",
"sqlab.myshopify.com",
"shopreyllen.myshopify.com",
"jinenstore.myshopify.com",
"cord-bands.myshopify.com",
"raffi-online.myshopify.com",
"gorillarobes-com.myshopify.com",
"luna-fied.myshopify.com",
"thealkemyst.myshopify.com",
"levonesofacover.myshopify.com",
"jalaclothing-com.myshopify.com",
"shophonu.myshopify.com",
"aromatech-canada.myshopify.com",
"lionparts.myshopify.com",
"the-whole-bride.myshopify.com",
"blowhammer-brand.myshopify.com",
"slyk-shades.myshopify.com",
"viggotailoring.myshopify.com",
"stilform.myshopify.com",
"bonvagonstore.myshopify.com",
"essentials-for-zula.myshopify.com",
"vajacases.myshopify.com",
"aidashoreditch.myshopify.com",
"poshpuppy-boutique.myshopify.com",
"malek-neman.myshopify.com",
"believe-accessories-inc.myshopify.com",
"shopluluandroo.myshopify.com",
"frankie-collective.myshopify.com",
"lowa-fi.myshopify.com",
"alquema.myshopify.com",
"microfiberwholesale.myshopify.com",
"ford-millinery.myshopify.com",
"the-laundry-room.myshopify.com",
"one-affirmation.myshopify.com",
"camillaandmarc-nz.myshopify.com",
"bows-and-arrows-co-llc.myshopify.com",
"peixoto-wear-shop.myshopify.com"
]

# Crawl the subdomains
results = crawl_shopify_subdomains(shopify_subdomains)

# Save results to a CSV file
import csv

output_file = "Shopify_Actual_Domains_Python.csv"
with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Shopify Subdomain", "Actual Domain"])
    writer.writerows(results)

print(f"Results saved to {output_file}")