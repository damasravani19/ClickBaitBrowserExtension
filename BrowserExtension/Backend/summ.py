import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import sys
# src_text = sys.argv[1]

# src_text = [
#     "Pop CultureQuizzesVideoLifestyleCommunityAboutCalling all ✨metal fans!✨✨BuzzFeed StaffWe hope you love the products we recommend! All of them were independently selected by our editors. Just so you know, BuzzFeed may collect a share of sales or other compensation from the links on this page if you decide to shop from them. Oh, and FYI — prices are accurate and items in stock as of time of publication.\n1.\nAdd texture to a plain wall with mirrored decals like these square or hexagon decals, available in silver or gold finishes, or these butterfly decals for a more romantic vibe.\nSquare mirror decals - ₹275 (set of 100)  Hexagon mirrored 3D wall stickers - ₹339 Butterfly decals - ₹349\n2.\nSpruce up your vanity with a golden mirrored tray, a brush holder or a tissue box.\nMirrored tray (8x6 inches) - ₹695Mirrored tray (9x7 inches) - ₹600Brush holder - ₹320 Tissue box - ₹899\n3.\nA stunning asymmetric pouffe - ₹2,099 available in a brass or iron finish, or a round pouffe - ₹1,995 can double up as seating, a footrest, or as a surface to keep books and more.\nBrand: Psygn. Colours and styles available. Get the asymmetrical pouffes here and the round pouffes here. From ₹2,775.You may also like: 31 Unique Pouffes And Ottomans To Level Up Your Home Decor\n4.\nThis stunning metal side table - ₹1,999 with an elegant wood surface is ideal for holding small objects like that book you can barely put down and the cup of tea to go with it.\nMetal side table - ₹1,999\n5.\nThis mid-century accent table with hairpin legs - ₹999.\nBrand: Casa Decor. Get it here for ₹999.\n6.\nA metal wall grid - ₹799 to put up your to-dos, favourite memes and posters.\nMetal wall grid - ₹799\n7.\nAdd a pop of the whimsical, like this stylish and functional pineapple jar - ₹1,499\nVelleitie Pineapple Jar - ₹1,499\n8.\nThis dispensing jar - ₹1,154 that's so pretty it'll motivate you to drink more water or make some agua fresca.\nDispensing jar - ₹1,154\n9.\nThese 30-foot long string lights - ₹99 to keep your space feeling cosy and festive.\n30-foot long string lights - ₹99\n10.\nThis sleek, triangular magazine holder to organise mags, files, and more - ₹749\nGet it here.\n11.\nThe chic, affordable IKEA ADDE Chair or IKEA MARIUS Stool. They're lightweight, easy to carry, space-saving (you can stack them one on top of the other) and suitable for both indoor and outdoor use. Available in four colours.\nIKEA ADDE Chair - ₹1,147IKEA MARIUS Stool - ₹595\n12.\nA must-have accessory to nail this look is a gorgeous sunburst mirror, and this golden coloured one would light up your whole space - ₹1,999\nGet it here.\n13.\nThese natural agate coasters - ₹1,495 (Set of 4) with a golden border that look positively ethereal and come equipped with transparent silicone felts at the bottom have silicone felt bottoms to protect furniture surfaces.\nNatural agate coasters - ₹1,495 (Set of 4)\n14.\nDecorative brass candlestick holders - ₹399 are a popular mid-century modern home accessory. Pair them with old school taper candles - ₹250\nBrass candlestick holders - ₹399Taper candles - ₹250\n15.\nThis round coffee table - ₹4,955, metal with a wood surface, is both glam and earthy. It's available in several finishes.\nCoffee table - ₹4,955\n16.\nYou may also like these nesting coffee tables - ₹14,339 with a gold frame and glass top.\nNesting coffee tables - ₹14,339\n17.\nThis black console - ₹13,900 with a metal frame will add some serious oomph to your foyer!\nSamDecors Black Console - ₹13,900\n18.\nUse pretty trays to place organise smaller items on your coffee table, like candles and remotes.\nGRD Round Tray -₹1,175GiftingBestWishes gold laser cut tray - ₹620\n19.\nFor your coffee table, add these gothic, art deco black-and-gold paperbacks of classics like Metamorphosis or The Great Gatsby.\nMetamorphosis by Franz Kafka - ₹79 The Great Gatsby by F Scott Fitzgerald - ₹79\n20.\nThis dark brown and gold photo frame - ₹99 so you can see your favourite moments and people every day.\nBrown and gold photo frame - ₹99\n21.\nFor a sleek lighting fixture, how about this Sputnik chandelier? An iconic mid-century modern fixture, named after the 1957 satellite, it goes well with this style due to the simplicity of the metal and glass and exposed look.\nGet it here:Sputnik chandelier - ₹4,700\n22.\nThis industrial, brass 'Fireworm' lamp - ₹1,250, handcrafted by artisans.\nGet it here.\n23.\nThe IKEA PS2014 pendant lamp has a unique geometric silhouette and is available in white - ₹3,999 and copper - ₹8,599. It will lend an art deco touch to any space.\nGet the IKEA PS2014 lamp here:White - ₹3,999 Copper - ₹8,599\n24.\nIf you love tealight candles, do get this golden Home Centre Moksha hanging lantern - ₹249, available in several colours. It has 1000+ reviews!\nGet it here:Home Centre Moksha hanging lantern - ₹249\n25.\nAdd a pop of the ornate with this handcrafted mirror - ₹2,499 in a distressed, dull gold finish.\n59.5 x 59.5 x 1.5 cmGet it here:Dull golden mirror - ₹2,499\n26.\nSome simple, airtight glass jars - ₹699 for 4 will make your storebought items look like you grew them yourself and keep them lasting long.\nGlass jars - ₹699 for 4\n27.\nInvest in this little metal storage trunk, that's both practical and decorative!\nGet it here:Elan metal storage trunk - ₹1,799\n28.\nGolden terrarium holders - ₹799 will add a sophisticated touch to your indoor garden.\nGolden terrarium holders - ₹799\n29.\nThese trendy metallic planters - ₹777 to show off your green thumb.\nMetallic planters - ₹777\n30.\nAn interesting animal-head brass knocker will add some interest to a basic door.\nLion brass knocker - ₹599Eagle brass knocker - ₹895Deer brass knocker - ₹865\n31.\nFinally, bed with a sleek wrought iron bed frame goes well with a variety of styles from industrial to art deco, as you please!\nFurnitureKraft Osaka Single Size Metal Bed - ₹4,489FurnitureKraft Zurich Metal Queen - ₹5,999FurnitureKraft King Bed - ₹7,050Share This Article"
# ]
src_text=[]
src_text.append(sys.argv[1])
model_name = 'google/pegasus-xsum'
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)
batch = tokenizer.prepare_seq2seq_batch(src_text, truncation=True, padding='longest', return_tensors="pt").to(torch_device)
translated = model.generate(**batch)
tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)

f=open("output.txt","w+")
f.write(tgt_text[0])
# assert tgt_text[0] == "California's largest electricity provider has turned off power to hundreds of thousands of customers."