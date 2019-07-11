# Form Maker
1. Post form JSON to URL
2. Lambda creates HTML from JSON and returns it

Example JSON:
```
{
    "class": "form",
    "inputs": [
        {
            "name": "name",
            "label": "Name",
            "placeholder": "Enter your name",
            "type": "text",
            "classes": "form-input",
            "id": "form-name"
        },
        {
            "name": "email",
            "label": "Email",
            "placeholder": "Enter your email",
            "type": "email",
            "classes": "form-input",
            "id": "form-email"
        },
        {
            "name": "country",
            "label": "Country",
            "placeholder": "Enter your country",
            "type": "select",
            "classes": "form-input",
            "id": "form-country",
            "options": [
                {
                    "value": "USA",
                    "name": "The States"
                },
                {
                    "value": "UK",
                    "name": "United Kingdom"
                },
                {
                    "value": "NE",
                    "name": "The Netherlands"
                }
            ]
        },
        {
            "name": "message",
            "label": "Message",
            "placeholder": "Enter Message",
            "type": "textarea",
            "classes": "form-textarea",
            "id": "form-message"
        }
    ], 
    "action": {
        "url": "default"
    },
    "method": "POST",
    "processActions": [
        {
            "action": "email",
            "to": "stuart.mason@pfizer.com"
        }
    ]
}
```

Example Form:
```
<div class="container">
  <form action="https://actions.aws.com/actionthisemail">

    <label for="fname">First Name</label>
    <input type="text" id="fname" name="firstname" placeholder="Your name..">

    <label for="lname">Last Name</label>
    <input type="text" id="lname" name="lastname" placeholder="Your last name..">

    <label for="country">Country</label>
    <select id="country" name="country">
      <option value="australia">Australia</option>
      <option value="canada">Canada</option>
      <option value="usa">USA</option>
    </select>

    <label for="subject">Subject</label>
    <textarea id="subject" name="subject" placeholder="Write something.."></textarea>

    <input type="submit" value="Submit">

  </form>
</div>
```