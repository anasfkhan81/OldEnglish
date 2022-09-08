<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:dc="http://purl.org/dc/elements/1.1/">
<xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"  standalone="yes" doctype-system="http://globalwordnet.github.io/schemas/WN-LMF-1.0.dtd"/>
<xsl:strip-space elements="*"/>

<xsl:template match="@*|node()">
  <xsl:copy>
    <xsl:apply-templates select="@*|node()"/>
  </xsl:copy>
</xsl:template>

<xsl:template match="SenseDefinition"/>
<xsl:template match="Etymology"/>
<xsl:template match="@grammaticalGender"/>
<xsl:template match="@partOfSpeech"/>
<xsl:template match="//Lemma">
    <Lemma partOfSpeech="{//LexicalEntry/@partOfSpeech}">
       <xsl:apply-templates select="@* | node()"/>
    </Lemma>
 </xsl:template>

</xsl:stylesheet>
