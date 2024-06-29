1. Fonksiyon Tanımlama ve Prototip
Fonksiyon tanımlamak, bir işlevin ne yapacağını tanımlamak ve programınıza belirli bir işlevsellik eklemek için kullanılır. Bir fonksiyon genellikle şu bileşenleri içerir:

cpp
Copy code
// Fonksiyon prototipi (deklarasyonu)
int add(int a, int b);

// Fonksiyon tanımı (definition)
int add(int a, int b) {
    return a + b;
}
Fonksiyon Prototipi (Deklarasyonu):

int add(int a, int b);
Fonksiyonun varlığını ve imzasını bildiren bir bildirimdir.
Genellikle fonksiyonun kullanılacağı yerden önce yer alır.
İmza, fonksiyonun adı ve parametre listesinden oluşur, dönüş türü de belirtilir.
Fonksiyon Tanımı (Definition):

int add(int a, int b) { return a + b; }
Fonksiyonun gerçek işlevini ve kodunu tanımlayan kısımdır.
İmza ile aynı olmalıdır.
Tanımlama, fonksiyonun ne yapacağını belirtir.
2. Fonksiyon Parametreleri
Fonksiyonlar, parametreler aracılığıyla bilgi alıp işleyebilir:

cpp
Copy code
void greet(const std::string& name) {
    std::cout << "Hello, " << name << "!" << std::endl;
}
Parametreler:
const std::string& name
Fonksiyona geçirilen değerleri almak için kullanılır.
Parametre isimleri ve tipleri tanımlama kısmında belirtilir.
const ile işaretlenmiş parametreler değiştirilemez (const correctness).
3. Dönüş Türü
Fonksiyonlar, işlemlerini tamamladıktan sonra bir değer dönebilirler:

cpp
Copy code
int add(int a, int b) {
    return a + b;
}
Dönüş Türü:
int
Fonksiyonun çağrıldığında geri döndüreceği değerin türünü belirtir.
Dönüş türü olmayan fonksiyonlar için void kullanılır.
4. Fonksiyon Overloading
Aynı isimde fakat farklı parametre listeleriyle birden fazla fonksiyon tanımlanabilir:

cpp
Copy code
int add(int a, int b) {
    return a + b;
}

double add(double a, double b) {
    return a + b;
}
Fonksiyon Aşırı Yükleme (Function Overloading):
Farklı parametre listeleri ile aynı ada sahip birden fazla fonksiyon tanımlamak.
Derleyici, fonksiyon çağrısının parametre listesine göre hangi fonksiyonun çağrılacağını belirler.
5. Varsayılan Argümanlar
Fonksiyonlara varsayılan argümanlar atanabilir:

cpp
Copy code
void printMessage(std::string msg = "Hello") {
    std::cout << msg << std::endl;
}
Varsayılan Argümanlar:
msg = "Hello"
Eğer fonksiyon çağrısında bu argüman belirtilmezse, varsayılan değer kullanılır.
6. Fonksiyon İşaretçileri ve Fonksiyon Göstericileri
Fonksiyon işaretçileri, fonksiyonları işaret eden değişkenlerdir:

cpp
Copy code
int (*funcPtr)(int, int); // Fonksiyon işaretçisi tanımı

int add(int a, int b) {
    return a + b;
}

funcPtr = &add; // İşaretçiye fonksiyon atanması
int result = (*funcPtr)(3, 5); // İşaretçiyle fonksiyon çağrısı
Fonksiyon İşaretçileri (Function Pointers):
Fonksiyon adreslerini saklamak ve çağırmak için kullanılır.
İşaretçi tanımlamak, işaretçiye bir fonksiyon atamak ve işaretçiyle fonksiyon çağırmak gibi adımlar içerir.
7. İç İşlevler (Inner Functions)
Bir fonksiyonun içinde başka bir fonksiyon tanımlanabilir:

cpp
Copy code
void outerFunction() {
    void innerFunction() {
        std::cout << "Inner function called." << std::endl;
    }
    innerFunction(); // İç fonksiyon çağrısı
}
İç İşlevler (Inner Functions):
Bir fonksiyonun içinde tanımlanan ve sadece o fonksiyonun içinde erişilebilen başka bir fonksiyondur.
Genellikle kapsülleme ve kod organizasyonu için kullanılır.
8. Lambdalar (Lambdas)
Anonim fonksiyonlar olarak bilinen lambdalar, kısa işlevsel parçaları temsil eder:

cpp
Copy code
auto add = [](int a, int b) {
    return a + b;
};

int result = add(3, 5); // Lambda fonksiyonu çağrısı
Lambdalar (Lambdas):
İsimsiz (anonim) fonksiyonlardır.
Kısa işlevsel kod parçalarını temsil ederler ve inline olarak kullanılabilirler.
Capture listesi ile dış değişkenleri yakalayabilirler.


9. Static Fonksiyonlar
Bir fonksiyon static olarak tanımlanırsa, bu fonksiyon sınıfın bir üyesi olmaksızın çağrılabilir:

cpp
Copy code
class MyClass {
public:
    static void staticFunction() {
        std::cout << "Static function called." << std::endl;
    }
};

MyClass::staticFunction(); // Static fonksiyon çağrısı
Static Fonksiyonlar:
Sınıfın bir üyesi olmaksızın, sınıf adıyla doğrudan çağrılabilirler.
Sınıfın herhangi bir örneği oluşturulmadan kullanılabilirler.



10. Fonksiyon Şablonları (Function Templates)
Fonksiyon şablonları, genel bir fonksiyon şablonu sağlar ve birden fazla veri türüyle çalışabilir:

cpp
Copy code
template <typename T>
T max(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    int maxInt = max(3, 5);
    double maxDouble = max(3.5, 2.7);
    return 0;
}
Fonksiyon Şablonları (Function Templates):
Genel bir fonksiyon şablonu tanımlar.
template <typename T> ile başlar ve farklı veri türleriyle kullanılabilir.
Çalışma zamanında tür parametreleriyle özelleştirilir.
11. Fonksiyonların İletişimi ve Kapsamı
Fonksiyonlar, global veya yerel kapsamda tanımlanabilir ve birbirleriyle iletişim kurabilirler:

cpp
Copy code
int globalVariable = 10;

void foo() {
    int localVariable = 5;
    globalVariable = localVariable + 5;
}

int main() {
    foo();
    std::cout << "Global variable: " << globalVariable << std::endl;
    return 0;
}
Fonksiyonların İletişimi ve Kapsamı:
Global değişkenlere erişilebilir.
Fonksiyonlar, aynı dosya içinde veya farklı dosyalarda tanımlanabilirler.
12. Fonksiyonların Geçirilmesi ve Geri Döndürülmesi
Fonksiyonlar, başka fonksiyonlara argüman olarak geçirilebilir veya başka fonksiyonlardan döndürülebilir:

cpp
Copy code
void process(int (*funcPtr)(int, int)) {
    int result = funcPtr(3, 5);
    std::cout << "Result: " << result << std::endl;
}

int add(int a, int b) {
    return a + b;
}

int main() {
    process(add);
    return 0;
}
Fonksiyonların Geçirilmesi ve Geri Döndürülmesi:
İşaretçi kullanarak veya fonksiyon nesnesi döndürerek bir fonksiyon başka bir fonksiyona geçirilebilir veya geri döndürülebilir.
13. Fonksiyon Hataları ve İstisnalar
Fonksiyonlar hatalar ve istisnalar yönetilebilir:

cpp
Copy code
double divide(double a, double b) {
    if (b == 0.0)
        throw std::runtime_error("Division by zero");
    return a / b;
}

int main() {
    try {
        double result = divide(10.0, 0.0);
    } catch (const std::runtime_error& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }
    return 0;
}
Fonksiyon Hataları ve İstisnalar:
Hata durumlarını işlemek için throw ifadesi kullanılır.
try-catch blokları ile istisnalar yakalanabilir ve işlenebilir.

14. Inline Fonksiyonlar
Küçük, sıkça kullanılan fonksiyonlar inline olarak tanımlanabilir:

cpp
Copy code

inline int add(int a, int b) {
    return a + b;
}

Inline Fonksiyonlar:
Küçük işlevlerin, derleme sırasında doğrudan yerine konması için inline anahtar kelimesi kullanılır.
Performansı artırabilir, ancak fonksiyonun tanımı her dosyada mevcut olmalıdır.

15. Özel Fonksiyonlar
Bazı özel durumlar için C++ dilinde özel fonksiyonlar tanımlanabilir:

cpp
Copy code
class MyClass {
public:
    // Default constructor
    MyClass() {
        std::cout << "Default constructor called." << std::endl;
    }

    // Copy constructor
    MyClass(const MyClass& other) {
        std::cout << "Copy constructor called." << std::endl;
    }

    // Destructor
    ~MyClass() {
        std::cout << "Destructor called." << std::endl;
    }

    // Operator overloading
    MyClass& operator=(const MyClass& other) {
        std::cout << "Assignment operator called." << std::endl;
        return *this;
    }
};
Özel Fonksiyonlar:
Sınıfın yaşam döngüsünü, kopyalama, atanma, yok etme gibi özel durumları için tanımlanabilirler.
Sınıfın belirli davranışlarını özelleştirmek için kullanılırlar.


16. Fonksiyonların Modüler Kullanımı
Fonksiyonlar, modüler programlama için önemli bir araçtır ve kodun tekrar kullanılabilirliğini artırır:

cpp
Copy code
// MathFunctions.h
#ifndef MATH_FUNCTIONS_H
#define MATH_FUNCTIONS_H

namespace Math {
    int add(int a, int b);
    int subtract(int a, int b);
    double multiply(double a, double b);
    double divide(double a, double b);
}

#endif // MATH_FUNCTIONS_H

// MathFunctions.cpp
#include "MathFunctions.h"

namespace Math {
    int add(int a, int b) {
        return a + b;
    }

    int subtract(int a, int b) {
        return a - b;
    }

    double multiply(double a, double b) {
        return a * b;
    }

    double divide(double a, double b) {
        if (b == 0.0)
            throw std::runtime_error("Division by zero");
        return a / b;
    }
}

// main.cpp
#include <iostream>
#include "MathFunctions.h"

int main() {
    std::cout << "Addition: " << Math::add(3, 5) << std::endl;
    std::cout << "Subtraction: " << Math::subtract(10, 5) << std::endl;
    std::cout << "Multiplication: " << Math::multiply(2.5, 4.0) << std::endl;
    
    try {
        std::cout << "Division: " << Math::divide(10.0, 2.0) << std::endl;
    } catch (const std::runtime_error& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }

    return 0;
}
Fonksiyonların Modüler Kullanımı:
Fonksiyonlar, farklı dosyalarda tanımlanabilir ve header dosyaları ile diğer dosyalarda kullanılabilir.
Modüler programlama yaklaşımını destekler, kodun organizasyonunu ve bakımını kolaylaştırır.
17. Fonksiyonlar ve Bellek Yönetimi
Fonksiyonlar, dinamik bellek yönetimi ve ömrü boyunca doğru bellek kullanımını sağlamak için kullanılabilir:

cpp
Copy code
#include <iostream>

int* createArray(int size) {
    int* arr = new int[size];
    for (int i = 0; i < size; ++i) {
        arr[i] = i * 2;
    }
    return arr;
}

void printArray(int* arr, int size) {
    for (int i = 0; i < size; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    delete[] arr; // Belleği serbest bırakma
}

int main() {
    int* arr = createArray(5);
    printArray(arr, 5);
    return 0;
}
Fonksiyonlar ve Bellek Yönetimi:
Dinamik bellek yönetimi için fonksiyonlar kullanılabilir (new, delete).
Belleği doğru bir şekilde tahsis etmek ve serbest bırakmak önemlidir (delete veya delete[]).
18. İstisnalar ve Hata Yönetimi
Fonksiyonlar, hataları işlemek için try-catch blokları ve istisnalar kullanabilir:

cpp
Copy code
#include <iostream>
#include <stdexcept>

double divide(double a, double b) {
    if (b == 0.0)
        throw std::runtime_error("Division by zero");
    return a / b;
}

int main() {
    try {
        double result = divide(10.0, 0.0);
    } catch (const std::runtime_error& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }
    return 0;
}
İstisnalar ve Hata Yönetimi:
Fonksiyonlar, throw ifadesi ile hata durumlarını işaretler.
try-catch blokları ile istisnalar yakalanabilir ve işlenebilir.
19. Fonksiyonların Kapsamı ve Görünürlüğü
Fonksiyonlar, kapsamları ve görünürlükleriyle diğer kod parçalarıyla etkileşimde bulunabilir:

cpp
Copy code
#include <iostream>

namespace Math {
    int add(int a, int b) {
        return a + b;
    }
}

int main() {
    int result = Math::add(3, 5);
    std::cout << "Result: " << result << std::endl;
    return 0;
}
Fonksiyonların Kapsamı ve Görünürlüğü:
Fonksiyonlar, global alanlar veya isim alanları içinde tanımlanabilir.
namespace, class veya struct gibi yapılarla kapsamları belirlenebilir.
20. Fonksiyonların Çalışma Zamanı Performansı
Fonksiyonların performansı, inline fonksiyonlar ve derleyici optimizasyonları ile iyileştirilebilir:

cpp
Copy code
inline int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(3, 5);
    return 0;
}
Fonksiyonların Çalışma Zamanı Performansı:
Inline fonksiyonlar ve derleyici optimizasyonları, fonksiyon çağrılarının performansını artırabilir.
Fakat fonksiyonların inline olarak tanımlanması, derleyici optimizasyonlarına ve kod tekrarlamasına bağlıdır.
21. Fonksiyon Şablonlarının Özelleştirilmesi
Fonksiyon şablonları, farklı veri türleri için özelleştirilebilir:

cpp
Copy code
template <typename T>
T max(T a, T b) {
    return (a > b) ? a : b;
}

template <>
std::string max<std::string>(std::string a, std::string b) {
    return (a.length() > b.length()) ? a : b;
}

int main() {
    int maxInt = max(3, 5);
    std::string maxStr = max("apple", "orange");
    return 0;
}
Fonksiyon Şablonlarının Özelleştirilmesi:
Genel bir fonksiyon şablonunu belirli veri türleri için özelleştirmek için kullanılır.
Özelleştirilmiş şablonlar, genel şablondan farklı davranışlar gösterebilir.
22. Fonksiyonlar ve Çoklu Dosya Kullanımı
Bir programın farklı dosyaları arasında fonksiyonları paylaşmak ve kullanmak mümkündür:

cpp
Copy code
// MathFunctions.h
#ifndef MATH_FUNCTIONS_H
#define MATH_FUNCTIONS_H

namespace Math {
    int add(int a, int b);
    int subtract(int a, int b);
}

#endif // MATH_FUNCTIONS_H

// MathFunctions.cpp
#include "MathFunctions.h"

namespace Math {
    int add(int a, int b) {
        return a + b;
    }

    int subtract(int a, int b) {
        return a - b;
    }
}

// main.cpp
#include <iostream>
#include "MathFunctions.h"

int main() {
    int sum = Math::add(3, 5);
    int difference = Math::subtract(10, 5);
    std::cout << "Sum: " << sum << std::endl;
    std::cout << "Difference: " << difference << std::endl;
    return 0;
}
Fonksiyonlar ve Çoklu Dosya Kullanımı:
Fonksiyonlar, farklı dosyalar arasında header dosyaları ile paylaşılabilir ve kullanılabilir.
Derleyici, #include direktifleri ile gerekli dosyaları dahil ederek fonksiyonları birleştirir.
23. Fonksiyon Şablonlarının Derleme Zamanı Performansı
Fonksiyon şablonları, derleme zamanında işlenir ve tür parametreleriyle özelleştirilir:

cpp
Copy code
template <typename T>
T max(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    int maxInt = max(3, 5);
    double maxDouble = max(3.5, 2.7);
    return 0;
}
Fonksiyon Şablonlarının Derleme Zamanı Performansı:
Fonksiyon şablonları, derleme zamanında tür parametreleri ile özelleştirilir.
Bu, kodun farklı veri türleri için etkin ve optimize edilmiş halini sağlar.
24. Fonksiyon Türleri ve Modern C++ Özellikleri
Modern C++ ile gelen yeni özellikler, fonksiyonların kullanımını ve tanımlanmasını daha güçlü hale getirir:

cpp
Copy code
#include <iostream>
#include <functional>

void process(int num, std::function<int(int)> func) {
    int result = func(num);
    std::cout << "Result: " << result << std::endl;
}

int addOne(int num) {
    return num + 1;
}

int main() {
    process(5, addOne);
    return 0;
}
Fonksiyon Türleri ve Modern C++ Özellikleri:
std::function ve lambda ifadeleri gibi modern C++ özellikleri, fonksiyonları daha esnek bir şekilde kullanmayı sağlar.
Fonksiyonları parametre olarak geçirip döndürmek, modern C++'da yaygın bir yaklaşımdır.
25. Fonksiyonların İç İşlevleri ve Kapsamı
Bir fonksiyonun içinde başka bir fonksiyon tanımlamak, sadece o kapsam içinde erişilebilir bir iç işlev oluşturur:

cpp
Copy code
#include <iostream>

void outerFunction() {
    void innerFunction() {
        std::cout << "Inner function called." << std::endl;
    }
    innerFunction(); // İç fonksiyon çağrısı
}

int main() {
    outerFunction();
    return 0;
}
Fonksiyonların İç İşlevleri ve Kapsamı:
İç işlevler, bir fonksiyonun içinde tanımlanan ve sadece o fonksiyonun içinde erişilebilen başka bir fonksiyondur.
Genellikle kod organizasyonunu ve gizliliği artırmak için kullanılırlar.
26. Fonksiyon Referansları ve Göstericileri
Fonksiyon göstericileri ve referansları, fonksiyonların adreslerini saklamak ve geçmek için kullanılır:

cpp
Copy code
#include <iostream>

int add(int a, int b) {
    return a + b;
}

void process(int a, int b, int (*funcPtr)(int, int)) {
    int result = funcPtr(a, b);
    std::cout << "Result: " << result << std::endl;
}

int main() {
    int (*funcPtr)(int, int) = &add;
    process(3, 5, funcPtr);
    return 0;
}
Fonksiyon Referansları ve Göstericileri:
Fonksiyon göstericileri, bir fonksiyonun adresini saklamak ve başka bir fonksiyona parametre olarak geçmek için kullanılır.
& operatörü ile fonksiyon adresi alınabilir.
27. Fonksiyonların Dahili Bellek Yönetimi
Fonksiyonlar, bellek yönetimi için dahili işlevler kullanabilir:

cpp
Copy code
#include <iostream>

int* createArray(int size) {
    int* arr = new int[size];
    for (int i = 0; i < size; ++i) {
        arr[i] = i * 2;
    }
    return arr;
}

void printArray(int* arr, int size) {
    for (int i = 0; i < size; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    delete[] arr; // Belleği serbest bırakma
}

int main() {
    int* arr = createArray(5);
    printArray(arr, 5);
    return 0;
}
Fonksiyonların Dahili Bellek Yönetimi:
Fonksiyonlar, dinamik bellek yönetimi için new ve delete operatörlerini kullanabilir.
Belleği doğru şekilde tahsis etmek ve serbest bırakmak önemlidir (delete veya delete[]).
28. Fonksiyonların Çok Biçimliliği ve Şablonları
Fonksiyon şablonları, tür parametreleriyle çok biçimliliği sağlar:

cpp
Copy code
template <typename T>
T max(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    int maxInt = max(3, 5);
    double maxDouble = max(3.5, 2.7);
    return 0;
}
Fonksiyonların Çok Biçimliliği ve Şablonları:
Fonksiyon şablonları, farklı veri türleri için tek bir şablon tanımlamayı ve kodun tekrar kullanılabilirliğini artırmayı sağlar.
Derleme zamanında tür parametreleri ile özelleştirilirler.
29. Fonksiyonlar ve Bellek Yönetimi
Fonksiyonlar, bellek yönetimi için dinamik bellek tahsisini ve serbest bırakmayı sağlar:

cpp
Copy code
#include <iostream>

int* createArray(int size) {
    int* arr = new int[size];
    for (int i = 0; i < size; ++i) {
        arr[i] = i * 2;
    }
    return arr;
}

void printArray(int* arr, int size) {
    for (int i = 0; i < size; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    delete[] arr; // Belleği serbest bırakma
}

int main() {
    int* arr = createArray(5);
    printArray(arr, 5);
    return 0;
}
Fonksiyonlar ve Bellek Yönetimi:
Dinamik bellek yönetimi için fonksiyonlar, new ve delete operatörlerini kullanabilir.
Belleği doğru şekilde tahsis etmek ve serbest bırakmak önemlidir (delete veya delete[]).
30. Fonksiyonların Geri Dönüş Değerleri ve İşlemleri
Fonksiyonlar, geri dönüş değerleri ve işlemleri ile programdaki işlevlerini yerine getirir:

cpp
Copy code
#include <iostream>

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int main() {
    int sum = add(3, 5);
    int difference = subtract(10, 5);
    std::cout << "Sum: " << sum << std::endl;
    std::cout << "Difference: " << difference << std::endl;
    return 0;
}
Fonksiyonların Geri Dönüş Değerleri ve İşlemleri:
Fonksiyonlar, belirli bir işlevi gerçekleştirir ve bir değer döndürebilir (return ifadesi ile).
Geri dönüş değeri, fonksiyonun çalışmasının sonucunu temsil eder.
31. Fonksiyonların Kapsamı ve Görünürlüğü
Fonksiyonlar, kapsam ve görünürlük kurallarına göre farklı dosyalar ve yapılar içinde tanımlanabilir:

cpp
Copy code
#include <iostream>

namespace Math {
    int add(int a, int b) {
        return a + b;
    }
}

int main() {
    int result = Math::add(3, 5);
    std::cout << "Result: " << result << std::endl;
    return 0;
}
Fonksiyonların Kapsamı ve Görünürlüğü:
Fonksiyonlar, global alanda veya isim alanları içinde tanımlanabilir.
namespace, class, veya struct gibi yapılar, fonksiyonların kapsamını belirler.
32. Fonksiyon Göstericileri ve Referansları
Fonksiyon göstericileri ve referansları, fonksiyonların adreslerini saklamak ve geçmek için kullanılır:

cpp
Copy code
#include <iostream>

int add(int a, int b) {
    return a + b;
}

void process(int a, int b, int (*funcPtr)(int, int)) {
    int result = funcPtr(a, b);
    std::cout << "Result: " << result << std::endl;
}

int main() {
    int (*funcPtr)(int, int) = &add;
    process(3, 5, funcPtr);
    return 0;
}
Fonksiyon Göstericileri ve Referansları:
Fonksiyon göstericileri, bir fonksiyonun adresini saklamak ve başka bir fonksiyona parametre olarak geçmek için kullanılır.
& operatörü ile fonksiyon adresi alınabilir.
33. Fonksiyonların Parametreleri ve Çağrıları
Fonksiyonlar, parametreler ve çağrıları ile belirli bir işlevi gerçekleştirir:

cpp
Copy code
#include <iostream>

int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(3, 5);
    std::cout << "Result: " << result << std::endl;
    return 0;
}
Fonksiyonların Parametreleri ve Çağrıları:
Fonksiyonlar, belirli bir işlevi gerçekleştirmek için parametreleri alır ve bu parametrelerle çağrılır.
Parametreler, fonksiyonun işlemesi için gerekli verileri temsil eder.
34. Fonksiyonların İçsel Kullanımı ve Özelleştirmesi
Fonksiyonlar, içsel kullanım ve özelleştirme için çeşitli yaklaşımlar sağlar:

cpp
Copy code
#include <iostream>

void greet() {
    std::cout << "Hello, world!" << std::endl;
}

void greet(std::string name) {
    std::cout << "Hello, " << name << "!" << std::endl;
}

int main() {
    greet();
    greet("Alice");
    return 0;
}
Fonksiyonların İçsel Kullanımı ve Özelleştirmesi:
Fonksiyonlar, belirli bir işlevi yerine getirmek için kullanılabilir ve aynı zamanda farklı parametrelerle özelleştirilebilir.
İsim aşırı yükleme (function overloading), C++'da fonksiyonların farklı versiyonlarını tanımlamak için kullanılır.
35. Fonksiyonların Geri Dönüş Değeri ve Özelleştirmesi
Fonksiyonlar, geri dönüş değeri ve özelleştirmesi ile farklı işlevleri gerçekleştirebilir:

cpp
Copy code
#include <iostream>

int add(int a, int b) {
    return a + b;
}

double add(double a, double b) {
    return a + b;
}

int main() {
    int result1 = add(3, 5);
    double result2 = add(3.5, 2.7);
    std::cout << "Result 1: " << result1 << std::endl;
    std::cout << "Result 2: " << result2 << std::endl;
    return 0;
}
Fonksiyonların Geri Dönüş Değeri ve Özelleştirmesi:
Fonksiyonlar, farklı geri dönüş değerleri ve parametrelerle özelleştirilebilir.
İsim aşırı yükleme (function overloading), C++'da bu tür özelleştirme için kullanılır.
36. Fonksiyonların Türetilmesi ve Kullanımı
Fonksiyonlar, farklı türeler ve parametreler ile türetilebilir ve kullanılabilir:

cpp
Copy code
#include <iostream>

template <typename T>
T add(T a, T b) {
    return a + b;
}

int main() {
    int sumInt = add(3, 5);
    double sumDouble = add(3.5, 2.7);
    std::cout << "Sum (int): " << sumInt << std::endl;
    std::cout << "Sum (double): " << sumDouble << std::endl;
    return 0;
}
Fonksiyonların Türetilmesi ve Kullanımı:
Fonksiyon şablonları, farklı türler için özelleştirilebilir ve aynı işlevi farklı türlerde kullanmayı sağlar.
Bu, C++'ın çok biçimlilik (polymorphism) özelliğinden yararlanır.
37. Fonksiyonların Geri Dönüş Değerleri ve İşlemleri
Fonksiyonlar, geri dönüş değerleri ve işlemleri ile belirli bir işlevi gerçekleştirir:

cpp
Copy code
#include <iostream>

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int main() {
    int sum = add(3, 5);
    int difference = subtract(10, 5);
    std::cout << "Sum: " << sum << std::endl;
    std::cout << "Difference: " << difference << std::endl;
    return 0;
}
Fonksiyonların Geri Dönüş Değerleri ve İşlemleri:
Fonksiyonlar, belirli bir işlevi gerçekleştirir ve bir değer döndürebilir (return ifadesi ile).
Geri dönüş değeri, fonksiyonun çalışmasının sonucunu temsil eder.
38. Fonksiyon Göstericileri ve Referansları
Fonksiyon göstericileri ve referansları, fonksiyonların adreslerini saklamak ve geçmek için kullanılır:

cpp
Copy code
#include <iostream>

int add(int a, int b) {
    return a + b;
}

void process(int a, int b, int (*funcPtr)(int, int)) {
    int result = funcPtr(a, b);
    std::cout << "Result: " << result << std::endl;
}

int main() {
    int (*funcPtr)(int, int) = &add;
    process(3, 5, funcPtr);
    return 0;
}
Fonksiyon Göstericileri ve Referansları:
Fonksiyon göstericileri, bir fonksiyonun adresini saklamak ve başka bir fonksiyona parametre olarak geçmek için kullanılır.
& operatörü ile fonksiyon adresi alınabilir.
39. Fonksiyonların İçsel Kullanımı ve Özelleştirmesi
Fonksiyonlar, içsel kullanım ve özelleştirme için çeşitli yaklaşımlar sağlar:

cpp
Copy code
#include <iostream>

void greet() {
    std::cout << "Hello, world!" << std::endl;
}

void greet(std::string name) {
    std::cout << "Hello, " << name << "!" << std::endl;
}

int main() {
    greet();
    greet("Alice");
    return 0;
}
Fonksiyonların İçsel Kullanımı ve Özelleştirmesi:
Fonksiyonlar, belirli bir işlevi yerine getirmek için kullanılabilir ve aynı zamanda farklı parametrelerle özelleştirilebilir.
İsim aşırı yükleme (function overloading), C++'da fonksiyonların farklı versiyonlarını tanımlamak için kullanılır.
40. Fonksiyonların Geri Dönüş Değeri ve Özelleştirmesi
Fonksiyonlar, geri dönüş değeri ve özelleştirmesi ile farklı işlevleri gerçekleştirebilir:

cpp
Copy code
#include <iostream>

int add(int a, int b) {
    return a + b;
}

double add(double a, double b) {
    return a + b;
}

int main() {
    int result1 = add(3, 5);
    double result2 = add(3.5, 2.7);
    std::cout << "Result 1: " << result1 << std::endl;
    std::cout << "Result 2: " << result2 << std::endl;
    return 0;
}
Fonksiyonların Geri Dönüş Değeri ve Özelleştirmesi:
Fonksiyonlar, farklı geri dönüş değerleri ve parametrelerle özelleştirilebilir.
İsim aşırı yükleme (function overloading), C++'da bu tür özelleştirme için kullanılır.
41. Fonksiyonların Türetilmesi ve Kullanımı
Fonksiyonlar, farklı türeler ve parametreler ile türetilebilir ve kullanılabilir:

cpp
Copy code
#include <iostream>

template <typename T>
T add(T a, T b) {
    return a + b;
}

int main() {
    int sumInt = add(3, 5);
    double sumDouble = add(3.5, 2.7);
    std::cout << "Sum (int): " << sumInt << std::endl;
    std::cout << "Sum (double): " << sumDouble << std::endl;
    return 0;
}
Fonksiyonların Türetilmesi ve Kullanımı:
Fonksiyon şablonları, farklı türler için özelleştirilebilir ve aynı işlevi farklı türlerde kullanmayı sağlar.
Bu, C++'ın çok biçimlilik (polymorphism) özelliğinden yararlanır.
42. Fonksiyonların Parametreleri ve Çağrıları
Fonksiyonlar, parametreler ve çağrıları ile belirli bir işlevi gerçekleştirir:

cpp
Copy code
#include <iostream>

int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(3, 5);
    std::cout << "Result: " << result << std::endl;
    return 0;
}
Fonksiyonların Parametreleri ve Çağrıları:
Fonksiyonlar, belirli bir işlevi gerçekleştirmek için parametreleri alır ve bu parametrelerle çağrılır.
Parametreler, fonksiyonun işlemesi için gerekli verileri temsil eder.
43. Fonksiyonların İçsel Kullanımı ve Özelleştirmesi
Fonksiyonlar, içsel kullanım ve özelleştirme için çeşitli yaklaşımlar sağlar:

cpp
Copy code
#include <iostream>

void greet() {
    std::cout << "Hello, world!" << std::endl;
}

void greet(std::string name) {
    std::cout << "Hello, " << name << "!" << std::endl;
}

int main() {
    greet();
    greet("Alice");
    return 0;
}
Fonksiyonların İçsel Kullanımı ve Özelleştirmesi:
Fonksiyonlar, belirli bir işlevi yerine getirmek için kullanılabilir ve aynı zamanda farklı parametrelerle özelleştirilebilir.
İsim aşırı yükleme (function overloading), C++'da fonksiyonların farklı versiyonlarını tanımlamak için kullanılır.
44. Fonksiyonların Geri Dönüş Değeri ve Özelleştirmesi
Fonksiyonlar, geri dönüş değeri ve özelleştirmesi ile farklı işlevleri gerçekleştirebilir:

cpp
Copy code
#include <iostream>

int add(int a, int b) {
    return a + b;
}

double add(double a, double b) {
    return a + b;
}

int main() {
    int result1 = add(3, 5);
    double result2 = add(3.5, 2.7);
    std::cout << "Result 1: " << result1 << std::endl;
    std::cout << "Result 2: " << result2 << std::endl;
    return 0;
}
Fonksiyonların Geri Dönüş Değeri ve Özelleştirmesi:
Fonksiyonlar, farklı geri dönüş değerleri ve parametrelerle özelleştirilebilir.
İsim aşırı yükleme (function overloading), C++'da bu tür özelleştirme için kullanılır.
45. Fonksiyonların Türetilmesi ve Kullanımı
Fonksiyonlar, farklı türeler ve parametreler ile türetilebilir ve kullanılabilir:

cpp
Copy code
#include <iostream>

template <typename T>
T add(T a, T b) {
    return a + b;
}

int main() {
    int sumInt = add(3, 5);
    double sumDouble = add(3.5, 2.7);
    std::cout << "Sum (int): " << sumInt << std::endl;
    std::cout << "Sum (double): " << sumDouble << std::endl;
    return 0;
}
Fonksiyonların Türetilmesi ve Kullanımı:
Fonksiyon şablonları, farklı türler için özelleştirilebilir ve aynı işlevi farklı türlerde kullanmayı sağlar.
Bu, C++'ın çok biçimlilik (polymorphism) özelliğinden yararlanır.
46. Fonksiyonların Parametreleri ve Çağrıları
Fonksiyonlar, parametreler ve çağrıları ile belirli bir işlevi gerçekleştirir:

cpp
Copy code
#include <iostream>

int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(3, 5);
    std::cout << "Result: " << result << std::endl;
    return 0;
}
Fonksiyonların Parametreleri ve Çağrıları:
Fonksiyonlar, belirli bir işlevi gerçekleştirmek için parametreleri alır ve bu parametrelerle çağrılır.
Parametreler, fonksiyonun işlemesi için gerekli verileri temsil eder.
47. Fonksiyonların İçsel Kullanımı ve Özelleştirmesi
Fonksiyonlar, içsel kullanım ve özelleştirme için çeşitli yaklaşımlar sağlar:

cpp
Copy code
#include <iostream>

void greet() {
    std::cout << "Hello, world!" << std::endl;
}

void greet(std::string name) {
    std::cout << "Hello, " << name << "!" << std::endl;
}

int main() {
    greet();
    greet("Alice");
    return 0;
}
Fonksiyonların İçsel Kullanımı ve Özelleştirmesi:
Fonksiyonlar, belirli bir işlevi yerine getirmek için kullanılabilir ve aynı zamanda farklı parametrelerle özelleştirilebilir.
İsim aşırı yükleme (function overloading), C++'da fonksiyonların farklı versiyonlarını tanımlamak için kullanılır.
48. Fonksiyonların Geri Dönüş Değeri ve Özelleştirmesi
Fonksiyonlar, geri dönüş değeri ve özelleştirmesi ile farklı işlevleri gerçekleştirebilir:

cpp
Copy code
#include <iostream>

int add(int a, int b) {
    return a + b;
}

double add(double a, double b) {
    return a + b;
}

int main() {
    int result1 = add(3, 5);
    double result2 = add(3.5, 2.7);
    std::cout << "Result 1: " << result1 << std::endl;
    std::cout << "Result 2: " << result2 << std::endl;
    return 0;
}
Fonksiyonların Geri Dönüş Değeri ve Özelleştirmesi:
Fonksiyonlar, farklı geri dönüş değerleri ve parametrelerle özelleştirilebilir.
İsim aşırı yükleme (function overloading), C++'da bu tür özelleştirme için kullanılır.
49. Fonksiyonların Türetilmesi ve Kullanımı
Fonksiyonlar, farklı türeler ve parametreler ile türetilebilir ve kullanılabilir:

cpp
Copy code
#include <iostream>

template <typename T>
T add(T a, T b) {
    return a + b;
}

int main() {
    int sumInt = add(3, 5);
    double sumDouble = add(3.5, 2.7);
    std::cout << "Sum (int): " << sumInt << std::endl;
    std::cout << "Sum (double): " << sumDouble << std::endl;
    return 0;
}
Fonksiyonların Türetilmesi ve Kullanımı:
Fonksiyon şablonları, farklı türler için özelleştirilebilir ve aynı işlevi farklı türlerde kullanmayı sağlar.
Bu, C++'ın çok biçimlilik (polymorphism) özelliğinden yararlanır.
50. Fonksiyonların Parametreleri ve Çağrıları
Fonksiyonlar, parametreler ve çağrıları ile belirli bir işlevi gerçekleştirir:

cpp
Copy code
#include <iostream>

int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(3, 5);
    std::cout << "Result: " << result << std::endl;
    return 0;
}
Fonksiyonların Parametreleri ve Çağrıları:
Fonksiyonlar, belirli bir işlevi gerçekleştirmek için parametreleri alır ve bu parametrelerle çağrılır.
Parametreler, fonksiyonun işlemesi için gerekli verileri temsil eder.