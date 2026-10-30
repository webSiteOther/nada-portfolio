@echo off
chcp 65001 >nul
echo ===============================================================
echo     Nada Nasser Portfolio - Upload to GitHub
echo     المستودع: https://github.com/webSiteOther/nada-portfolio.git
echo ===============================================================
echo.
echo المستودع جاهز محلياً وجميع الملفات تم حفظها (Commit) بنجاح!
echo.
set /p TOKEN="الصقي الـ Personal Access Token الخاص بكِ هنا واضغطي Enter: "
if "%TOKEN%"=="" (
    echo لم يتم إدخال الرمز.
    pause
    exit /b
)

echo.
echo جاري الرفع إلى GitHub...
"C:\flutter\bin\mingit\cmd\git.exe" push https://webSiteOther:%TOKEN%@github.com/webSiteOther/nada-portfolio.git main

if %ERRORLEVEL% equ 0 (
    echo.
    echo ===============================================================
    echo [تم بنجاح!] تم رفع البورتفوليو وجميع فولدرات المشاريع إلى GitHub!
    echo رابط مستودعك: https://github.com/webSiteOther/nada-portfolio
    echo ===============================================================
) else (
    echo.
    echo [تنبيه] فشل الرفع، تأكدي من صحة الـ Token وصلاحية 'repo'.
)
echo.
pause
