<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/flight">
  <html><body>
    <h1>Flight Info</h1>
    <p>Flight: <xsl:value-of select="number"/></p>
    <p>From: <xsl:value-of select="origin"/></p>
    <p>To: <xsl:value-of select="destination"/></p>
  </body></html>
</xsl:template>
</xsl:stylesheet>