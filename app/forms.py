from django import forms
from django.core import validators
from .models import User


class Register(forms.ModelForm):
    first_name = forms.CharField(required=True, help_text="Enter your First Name")
    last_name = forms.CharField(required=True)
    # email = forms.EmailField(required=True, validators=[validators.EmailValidator])
    age = forms.IntegerField(min_value=16, required=True)
    phone = forms.CharField(
        validators=[
            validators.RegexValidator(
                regex=r"[\d\+ ]{10,15}", message="Enter a valid phone number"
            )
        ]
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        validators=[
            validators.MinLengthValidator(6),
            validators.RegexValidator(
                regex=r"[a-z]+", message="Include atlease 1 lowercase letter"
            ),
            validators.RegexValidator(
                regex=r"[A-Z]+", message="Include atlease 1 uppercase letter"
            ),
            validators.RegexValidator(
                regex=r"[0-9]+", message="Include atlease 1 digit"
            ),
            validators.RegexValidator(
                regex=r"[@$!%*?&]+", message="Include atlease 1 special character"
            ),
        ],
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "age",
            "address",
            "phone",
        ]


class Login(forms.Form):
    username = forms.CharField(required=True, help_text="Enter your Username")
    password = forms.CharField(
        required=True, help_text="Enter your Password", widget=forms.PasswordInput()
    )


class ChangePwd(forms.Form):
    _password_validators = [
        validators.MinLengthValidator(6),
        validators.RegexValidator(
            regex=r"[a-z]+", message="Include atlease 1 lowercase letter"
        ),
        validators.RegexValidator(
            regex=r"[A-Z]+", message="Include atlease 1 uppercase letter"
        ),
        validators.RegexValidator(regex=r"[0-9]+", message="Include atlease 1 digit"),
        validators.RegexValidator(
            regex=r"[@$!%*?&]+", message="Include atlease 1 special character"
        ),
    ]

    password = forms.CharField(
        required=True,
        help_text="Enter a new Password",
        widget=forms.PasswordInput(),
        validators=_password_validators,
    )
    cnf_password = forms.CharField(
        required=True,
        help_text="Enter the Password again",
        widget=forms.PasswordInput(),
        label="Confirm Password",
        validators=_password_validators,
    )

    def clean(self):
        cleaned_data = super(ChangePwd, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("cnf_password")

        if password != confirm_password:
            raise forms.ValidationError(
                {
                    "password": "password and confirm_password does not match",
                    "cnf_password": "password and confirm_password does not match",
                }
            )
