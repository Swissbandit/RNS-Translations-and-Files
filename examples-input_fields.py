
## Fields and Submitting Data

Nomad Network let's you use simple input fields for submitting data to node-side applications. 
Submitted data, along with other session variables will be available to the node-side script / program as environment variables. 
This page contains a few examples.

## Read Environment Variables

## Examples of Fields and Submissions

The following section contains a simple set of fields, and a few different links that submit the field data in different ways.



An input field    : `B444`<username`Entered data>`b

An masked field   : `B444`<!|password`Value of Field>`b

An small field    : `B444`<8|small`test>`b, and some more text.

Two fields        : `B444`<8|one`One>`b `B444`<8|two`Two>`b

The data can be `!`[submitted`:/page/input_fields.mu`username|two]`!.

You can `!`[submit`:/page/input_fields.mu`one|password|small]`! other fields, or just `!`[a single one`:/page/input_fields.mu`username]`!

Or simply `!`[submit them all`:/page/input_fields.mu`*]`!.

Submission links can also `!`[include pre-configured variables`:/page/input_fields.mu`username|two|entitiy_id=4611|action=view]`!.

Or take all fields and `!`[pre-configured variables`:/page/input_fields.mu`*|entitiy_id=4611|action=view]`!.

Or only `!`[pre-configured variables`:/page/input_fields.mu`entitiy_id=4688|task=something]`!




from the nomadnet guide

Fields & Requests
Nomad Network let's you use simple input fields for submitting data to node-side applications. Submitted data, along with other session variables will be available to the node-side script / program as environment variables.
>>Request Links
Links can contain request variables and a list of fields to submit to the node-side application. You can include all fields on the page, only specific ones, and any number of request variables. To simply submit all fields on a page to a specified node-side page, create a link like this:
`Faaa
`=
`[Submit Fields`:/page/fields.mu`*]
`=
``
Note the `!*`! following the extra `!\``! at the end of the path. This `!*`! denotes `*all fields`*. You can also specify a list of fields to include:
`Faaa
`=
`[Submit Fields`:/page/fields.mu`username|auth_token]
`=
``
If you want to include pre-set variables, you can do it like this:
`Faaa
`=
`[Query the System`:/page/fields.mu`username|auth_token|action=view|amount=64]
`=
``
>> Fields
Here's an example of creating a field. We'll create a field named `!user_input`! and fill it with the text `!Pre-defined data`!. Note that we are using background color tags to make the field more visible to the user:
`Faaa
`=
A simple input field: `B444`<user_input`Pre-defined data>`b
`=
``
You must always set a field `*name`*, but you can of course omit the pre-defined value of the field:
`Faaa
`=
An empty input field: `B444`<demo_empty`>`b
`=
``
You can set the size of the field like this:
`Faaa
`=
A sized input field:  `B444`<16|with_size`>`b
`=
``
It is possible to mask fields, for example for use with passwords and similar:
`Faaa
`=
A masked input field: `B444`<!|masked_demo`hidden text>`b
`=
``
And you can of course control all parameters at the same time:
`Faaa
`=
Full control: `B444`<!32|all_options`hidden text>`b
`=
``
Collecting the above markup produces the following output:
`Faaa`B333
A simple input field: `B444`<user_input`Pre-defined data>`B333
An empty input field: `B444`<demo_empty`>`B333
A sized input field:  `B444`<16|with_size`>`B333
A masked input field: `B444`<!|masked_demo`hidden text>`B333
Full control: `B444`<!32|all_options`hidden text>`B333
``