from PIL import Image
import sys

def classify(image):
    img = Image.open(image)

    #resize to smaller image
    w,h = img.size
    img.resize((w//10,h//10)).save("tmp.jpg")
    img.close()

    img = Image.open("tmp.jpg")
    pix = img.load()

    w,h = img.size


    blue = [range(60,90),range(110,140),range(110,140)]
    red = [range(180,230), range(70,115), range(30,70)]
    green = [range(130,170),range(140,180), range(60,85)]
    yellow = [range(200,235), range(180,210), range(95,120)]
    pink = [range(210,240), range(150,180), range(110,130)]

    matte = "1TRQLR9GuNpmGa2CaGEJNlNzHkezDFZpg"
    fysikk = "1mJrIrr-feyaDjgunud8WkBYW21T2EGib"
    norsk = "1eYCvh6-chEbWjOVbvsjAtWjCyogco-M5"
    historie = "19YX0I_o7h5rYkTv_oEWNIepEt7mc7wx7"
    religion = "1t9Q8LGUfoJlYmYmm8-70jC82yA7S2x4f"
    felles = "felles"
    fag = []

    #check pixel rgb value, append blues to list
    for y in range(h):
        for x in range(w):
            r,g,b = pix[x,y]
            if r in blue[0] and g in blue[1] and b in blue[2]: 
                # print("BLUE",x,y)
                fag.append(matte)
                break
            elif r in red[0] and g in red[1] and b in red[2]:
                # print("RED",x,y)
                fag.append(fysikk)
                break
            elif r in green[0] and g in green[1] and b in green[2]:
                # print("GREEN", x,y)
                fag.append(norsk)
                break
            elif r in yellow[0] and g in yellow[1] and b in yellow[2]:
                # print("YELLOW",x,y)
                fag.append(historie)
                break
            elif r in pink[0] and g in pink[1] and b in pink[2]:
                # print("PINK",x,y)
                fag.append(religion)
                break
            else:
                pass
    return fag[0]

if __name__ == "__main__":
    arguments = sys.argv
    for argument in arguments:
        if argument == sys.argv[0]:
            pass
        else:
            print(argument, "=", classify(argument))
