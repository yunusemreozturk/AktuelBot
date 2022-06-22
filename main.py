"""
Bu program eğitim amaçlı oluşturulmuştur.
"""

import functions

while True:
    print('MENÜ'.center(50, '-'))
    try:
        choice = int(input('1- A101\n2- BİM\n3- ŞOK\n4- Exit\n\nSeçiminiz: '))
    except ValueError:
        print('Lütfen sayı giriniz.')
        print()
        continue
    print()

    if choice == 1:
        while True:
            count = 0
            classObject = functions.A101()
            link, title = classObject.home_page_returner()

            for item in title:
                count += 1
                print(f'{count}- {item}')
            print('4- Geri')

            try:
                choice2 = int(input('\nSeçiminiz: '))
            except ValueError or NameError:
                print('Lütfen sayı giriniz.')
                print()
                continue
            print()

            if choice2 == 4:
                break
            elif choice2 > 4:
                print('Yanlış bir giriş yaptınız.')
                print()
                continue

            result = classObject.content_page_loader(link[choice2 - 1])

            classObject.write_the_file(result)

            print(result)
            break

    elif choice == 2:
        while True:
            count = 0
            classObject = functions.BIM()
            link, title = classObject.home_page_returner()

            for item in title:
                count += 1
                print(f'{count}- {item}')
            print('4- Geri')

            try:
                choice2 = int(input('\nSeçiminiz: '))
            except ValueError or NameError:
                print('Lütfen sayı giriniz.')
                print()
                continue
            print()

            if choice2 == 4:
                break
            elif choice2 > 4:
                print('Yanlış bir giriş yaptınız.')
                print()
                continue

            result = classObject.content_page_loader(link[choice2 - 1])

            classObject.write_the_file(result)

            print(result)
            break

    elif choice == 3:
        while True:
            count = 0
            classObject = functions.SOK()
            link, title = classObject.home_page_returner()

            for item in title:
                count += 1
                print(f'{count}- {item}')
            print('4- Geri')

            try:
                choice2 = int(input('\nSeçiminiz: '))
            except ValueError or NameError:
                print('Lütfen sayı giriniz.')
                print()
                continue
            print()

            if choice2 == 4:
                break
            elif choice2 > 4:
                print('Yanlış bir giriş yaptınız.')
                print()
                continue

            result = classObject.content_page_loader(link[choice2 - 1])

            classObject.write_the_file(result)

            print(result)
            break

    elif choice == 4:
        break
    else:
        print('Yanlış bir giriş yaptınız.')
        continue
