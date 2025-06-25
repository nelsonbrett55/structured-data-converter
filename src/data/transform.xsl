<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:html="http://www.w3.org/1999/xhtml">
  <xsl:output method="html" indent="yes"/>

  <xsl:template match="/root">
    <html>
      <head>
        <title><xsl:value-of select="title"/> - <xsl:value-of select="company"/></title>
        <style>
          body { font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 2em; }
          h1 { color: #333; }
          table { width: 100%; border-collapse: collapse; margin-top: 1em; }
          th, td { padding: 10px; border: 1px solid #ccc; text-align: left; }
          th { background-color: #f0f0f0; }
          ul { margin: 0; padding-left: 1.2em; }
          li { margin-bottom: 4px; }
        </style>
      </head>
      <body>
        <h1><xsl:value-of select="title"/> - <xsl:value-of select="company"/></h1>

        <table>
          <tr>
            <th>Name</th>
            <th>Title</th>
            <th>Department</th>
            <th>Skills</th>
          </tr>
          <xsl:for-each select="employees/item">
            <xsl:sort select="name" order="ascending" />
            <tr>
              <td><xsl:value-of select="name"/></td>
              <td><xsl:value-of select="title"/></td>
              <td><xsl:value-of select="department"/></td>
              <td>
                <ul>
                  <xsl:for-each select="skills/item">
                    <li><xsl:value-of select="."/></li>
                  </xsl:for-each>
                </ul>
              </td>
            </tr>
          </xsl:for-each>
        </table>

        <p><em>Generated on <xsl:text>June 25, 2025</xsl:text></em></p>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>